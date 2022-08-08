import json
import os
from typing import List

import structlog

import orchestrator.computetask_pb2 as computetask_pb2
import orchestrator.model_pb2 as model_pb2
from substrapp.compute_tasks.context import Context
from substrapp.compute_tasks.context import TaskResource
from substrapp.compute_tasks.directories import SANDBOX_DIR
from substrapp.compute_tasks.directories import TaskDirName
from substrapp.models.image_entrypoint import ImageEntrypoint

logger = structlog.get_logger(__name__)

# These constants are shared with connect-tools.
# These constants will disappear once the inputs/outputs are exposed by the orchestrator.
TASK_IO_PREDICTIONS = "predictions"
TASK_IO_OPENER = "opener"
TASK_IO_LOCALFOLDER = "localfolder"
TASK_IO_CHAINKEYS = "chainkeys"
TASK_IO_DATASAMPLES = "datasamples"
TRAIN_IO_MODELS = "models"
TRAIN_IO_MODEL = "model"
COMPOSITE_IO_SHARED = "shared"
COMPOSITE_IO_LOCAL = "local"


class Filenames:
    OutModel = "out-model"
    OutHeadModel = "out-head-model"
    Opener = "__init__.py"
    Predictions = "pred.json"
    Performance = "perf.json"


TASK_COMMANDS = {
    computetask_pb2.TASK_TRAIN: "train",
    computetask_pb2.TASK_PREDICT: "predict",
    computetask_pb2.TASK_COMPOSITE: "train",
    computetask_pb2.TASK_AGGREGATE: "aggregate",
}


def get_performance_filename(algo_key: str) -> str:
    """Builds the performance filename

    Args:
        algo_key: The key of the algo that produce this performance file.

    Returns:
        A string representation of the performance filename.
    """
    return "-".join([algo_key, Filenames.Performance])


def get_exec_command(ctx: Context) -> List[str]:
    entrypoint = ImageEntrypoint.objects.get(algo_checksum=ctx.algo.checksum)

    command = entrypoint.entrypoint_json

    if command[0].startswith("python"):
        command.insert(1, "-u")  # unbuffered. Allows streaming the logs in real-time.

    args = _get_args(ctx)

    return command + args


# TODO: '_get_args' is too complex, consider refactoring
def _get_args(ctx: Context) -> List[str]:  # noqa: C901
    task = ctx.task
    task_category = ctx.task_category

    in_models_dir = os.path.join(SANDBOX_DIR, TaskDirName.InModels)
    out_models_dir = os.path.join(SANDBOX_DIR, TaskDirName.OutModels)
    openers_dir = os.path.join(SANDBOX_DIR, TaskDirName.Openers)
    datasamples_dir = os.path.join(SANDBOX_DIR, TaskDirName.Datasamples)
    local_folder = os.path.join(SANDBOX_DIR, TaskDirName.Local)
    chainkeys_folder = os.path.join(SANDBOX_DIR, TaskDirName.Chainkeys)

    inputs = []
    outputs = []

    if ctx.task_category == computetask_pb2.TASK_TEST:
        perf_path = os.path.join(SANDBOX_DIR, TaskDirName.Perf, get_performance_filename(ctx.algo.key))
        command = ["--input-predictions-path", os.path.join(in_models_dir, ctx.in_models[0]["key"])]
        command += ["--opener-path", os.path.join(openers_dir, ctx.data_manager["key"], Filenames.Opener)]
        command += ["--data-sample-paths"] + [os.path.join(datasamples_dir, key) for key in ctx.data_sample_keys]
        command += ["--output-perf-path", perf_path]
        # use a fake TaskResource until everything is properly passed as a generic output
        ctx.set_outputs([TaskResource(id="performance", value=perf_path)])
        return command

    compute_plan_key = None
    if "compute_plan_key" in task and task["compute_plan_key"]:
        compute_plan_key = task["compute_plan_key"]
    rank = str(task["rank"]) if compute_plan_key else None

    command = [TASK_COMMANDS[task_category]]

    if task_category == computetask_pb2.TASK_TRAIN:

        if ctx.in_models:
            inputs.extend(
                [
                    TaskResource(id=TRAIN_IO_MODELS, value=os.path.join(in_models_dir, model["key"]))
                    for model in ctx.in_models
                ]
            )

        inputs.append(
            TaskResource(id=TASK_IO_OPENER, value=os.path.join(openers_dir, ctx.data_manager["key"], Filenames.Opener))
        )
        for key in ctx.data_sample_keys:
            inputs.append(TaskResource(id=TASK_IO_DATASAMPLES, value=os.path.join(datasamples_dir, key)))
        outputs.append(TaskResource(id=TRAIN_IO_MODEL, value=os.path.join(out_models_dir, Filenames.OutModel)))
        outputs.append(TaskResource(id=TASK_IO_LOCALFOLDER, value=local_folder))

    elif task_category == computetask_pb2.TASK_COMPOSITE:

        for input_model in ctx.in_models:
            cat = model_pb2.ModelCategory.Value(input_model["category"])
            if cat == model_pb2.MODEL_HEAD:
                inputs.append(
                    TaskResource(id=COMPOSITE_IO_LOCAL, value=os.path.join(in_models_dir, input_model["key"]))
                )
            elif cat == model_pb2.MODEL_SIMPLE:
                inputs.append(
                    TaskResource(id=COMPOSITE_IO_SHARED, value=os.path.join(in_models_dir, input_model["key"]))
                )

        inputs.append(
            TaskResource(id=TASK_IO_OPENER, value=os.path.join(openers_dir, ctx.data_manager["key"], Filenames.Opener))
        )
        for key in ctx.data_sample_keys:
            inputs.append(TaskResource(id=TASK_IO_DATASAMPLES, value=os.path.join(datasamples_dir, key)))
        outputs.append(TaskResource(id=COMPOSITE_IO_LOCAL, value=os.path.join(out_models_dir, Filenames.OutHeadModel)))
        outputs.append(TaskResource(id=COMPOSITE_IO_SHARED, value=os.path.join(out_models_dir, Filenames.OutModel)))
        outputs.append(TaskResource(id=TASK_IO_LOCALFOLDER, value=local_folder))

    elif task_category == computetask_pb2.TASK_AGGREGATE:
        if ctx.in_models:
            inputs.extend(
                [
                    TaskResource(id=TRAIN_IO_MODELS, value=os.path.join(in_models_dir, model["key"]))
                    for model in ctx.in_models
                ]
            )

        outputs.append(TaskResource(id=TRAIN_IO_MODEL, value=os.path.join(out_models_dir, Filenames.OutModel)))
        outputs.append(TaskResource(id=TASK_IO_LOCALFOLDER, value=local_folder))

    elif task_category == computetask_pb2.TASK_PREDICT:
        for input_model in ctx.in_models:
            model_category = model_pb2.ModelCategory.Value(input_model["category"])
            identifier = None

            if model_category == model_pb2.MODEL_HEAD:
                identifier = COMPOSITE_IO_LOCAL
            elif model_category == model_pb2.MODEL_SIMPLE and len(ctx.in_models) == 2:
                identifier = COMPOSITE_IO_SHARED
            elif model_category == model_pb2.MODEL_SIMPLE:
                identifier = TRAIN_IO_MODELS
            else:
                raise ValueError(f"Invalid model category for predict task: {model_category}")

            inputs.append(TaskResource(id=identifier, value=os.path.join(in_models_dir, input_model["key"])))

        inputs.append(
            TaskResource(id=TASK_IO_OPENER, value=os.path.join(openers_dir, ctx.data_manager["key"], Filenames.Opener))
        )
        for key in ctx.data_sample_keys:
            inputs.append(TaskResource(id=TASK_IO_DATASAMPLES, value=os.path.join(datasamples_dir, key)))
        outputs.append(TaskResource(id=TASK_IO_PREDICTIONS, value=os.path.join(out_models_dir, Filenames.OutModel)))
        outputs.append(TaskResource(id=TASK_IO_LOCALFOLDER, value=local_folder))

    if rank and task_category != computetask_pb2.TASK_PREDICT:
        command += ["--rank", rank]
    if ctx.has_chainkeys:
        inputs.append(TaskResource(id=TASK_IO_CHAINKEYS, value=chainkeys_folder))

    ctx.set_outputs(outputs)

    command += ["--inputs", f"'{json.dumps(inputs)}'"]
    command += ["--outputs", f"'{json.dumps(outputs)}'"]

    logger.debug("Generated task command", command=command)

    return command
