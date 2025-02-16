"""
Utility module to create fixtures.

Basic example:

>>> algo = create_algo(
...     inputs=factory.build_algo_inputs(["datasamples", "opener", "model"]),
...     outputs=factory.build_algo_outputs(["model"]),
... )
>>> data_manager = create_datamanager()
>>> data_sample = create_datasample([data_manager])
>>> compute_plan = create_computeplan(status=ComputePlan.Status.PLAN_STATUS_DONE)

>>> train_task = create_computetask(
...     compute_plan,
...     algo,
...     inputs=factory.build_computetask_inputs(
...         algo,
...         {
...             "opener": [data_manager.key],
...             "datasamples": [data_sample.key],
...         },
...     ),
...     outputs=factory.build_computetask_outputs(algo),
...     data_manager=data_manager,
...     data_samples=[data_sample.key],
...     category=ComputeTask.Category.TASK_TRAIN,
...     status=ComputeTask.Status.STATUS_DONE,
... )
>>> model = create_model(train_task, identifier="model")

>>> metric = create_algo(
...     inputs=factory.build_algo_inputs(["datasamples", "opener", "model"]),
...     outputs=factory.build_algo_outputs(["performance"]),
... )
>>> test_task = create_computetask(
...     compute_plan,
...     metric,
...     inputs=factory.build_computetask_inputs(
...         metric,
...         {
...             "opener": [data_manager.key],
...             "datasamples": [data_sample.key],
...             "model": [train_task.key],
...         },
...     ),
...     outputs=factory.build_computetask_outputs(metric),
...     data_manager=data_manager,
...     data_samples=[data_sample],
...     parent_tasks=[train_task.key],
...     category=ComputeTask.Category.TASK_TEST,
...     status=ComputeTask.Status.STATUS_DONE,
... )
>>> performance = create_performance(test_task, metric, identifier="performance")

Customized example:

>>> algo_data = create_algo_files()
>>> algo = create_algo(
...     key=algo_data.key,
...     name="Random forest",
...     category=AlgoCategory.simple,
...     metadata={"foo": "bar"},
...     owner="MyOrg2MSP",
...     channel="yourchannel",
...     public="False",
... )
"""

import datetime
import uuid

from django.core import files
from django.utils import timezone

from api.models import Algo
from api.models import AlgoInput
from api.models import AlgoOutput
from api.models import ComputePlan
from api.models import ComputeTask
from api.models import ComputeTaskInput
from api.models import ComputeTaskInputAsset
from api.models import ComputeTaskOutput
from api.models import ComputeTaskOutputAsset
from api.models import DataManager
from api.models import DataSample
from api.models import Model
from api.models import Performance
from api.models import ProfilingStep
from api.models import TaskProfiling
from api.models.computetask import TaskDataSamples
from substrapp.models import Algo as AlgoFiles
from substrapp.models import ComputeTaskFailureReport as ComputeTaskLogs
from substrapp.models import DataManager as DataManagerFiles
from substrapp.models import DataSample as DataSampleFiles
from substrapp.models import Model as ModelFiles
from substrapp.utils import get_hash

DEFAULT_OWNER = "MyOrg1MSP"
DEFAULT_WORKER = "MyOrg1MSP"
DEFAULT_CHANNEL = "mychannel"
DUMMY_CHECKSUM = "dummy-checksum"


# Inputs and outputs values belongs to the business logic and are handled at the substra SDK level.
# We use them here only to have realistic test data, but the API should remained agnostic from them.

ALGO_INPUTS = {
    "datasamples": dict(kind=AlgoInput.Kind.ASSET_DATA_SAMPLE, multiple=True, optional=False),
    "opener": dict(kind=AlgoInput.Kind.ASSET_DATA_MANAGER, multiple=False, optional=False),
    "model": dict(kind=AlgoInput.Kind.ASSET_MODEL, multiple=False, optional=True),
    "models": dict(kind=AlgoInput.Kind.ASSET_MODEL, multiple=True, optional=True),
    "local": dict(kind=AlgoInput.Kind.ASSET_MODEL, multiple=False, optional=True),
    "shared": dict(kind=AlgoInput.Kind.ASSET_MODEL, multiple=False, optional=True),
    "predictions": dict(kind=AlgoInput.Kind.ASSET_MODEL, multiple=False, optional=False),
}
ALGO_OUTPUTS = {
    "model": dict(kind=AlgoOutput.Kind.ASSET_MODEL, multiple=False),
    "local": dict(kind=AlgoOutput.Kind.ASSET_MODEL, multiple=False),
    "shared": dict(kind=AlgoOutput.Kind.ASSET_MODEL, multiple=False),
    "predictions": dict(kind=AlgoOutput.Kind.ASSET_MODEL, multiple=False),
    "performance": dict(kind=AlgoOutput.Kind.ASSET_PERFORMANCE, multiple=False),
}


def build_algo_inputs(identifiers: list[str]) -> list[AlgoInput]:
    return [AlgoInput(identifier=identifier, **ALGO_INPUTS[identifier]) for identifier in identifiers]


def build_algo_outputs(identifiers: list[str]) -> list[AlgoOutput]:
    return [AlgoOutput(identifier=identifier, **ALGO_OUTPUTS[identifier]) for identifier in identifiers]


def build_computetask_inputs(
    algo: Algo,
    keys: dict[str : list[uuid.UUID]],
) -> list[ComputeTaskInput]:
    task_inputs = []
    for algo_input in algo.inputs.all():
        for key in keys.get(algo_input.identifier, []):
            task_input = ComputeTaskInput(identifier=algo_input.identifier)
            if algo_input.kind in (AlgoInput.Kind.ASSET_DATA_MANAGER, AlgoInput.Kind.ASSET_DATA_SAMPLE):
                task_input.asset_key = key
            else:  # we assume that all other assets are produced by parent tasks
                task_input.parent_task_key_id = key
                task_input.parent_task_output_identifier = algo_input.identifier
            task_inputs.append(task_input)
    return task_inputs


def build_computetask_outputs(
    algo: Algo,
    owner: str = DEFAULT_OWNER,
    public: bool = False,
) -> list[ComputeTaskOutput]:
    return [
        ComputeTaskOutput(
            identifier=algo_output.identifier,
            permissions_download_public=public,
            permissions_download_authorized_ids=[owner],
            permissions_process_public=public,
            permissions_process_authorized_ids=[owner],
        )
        for algo_output in algo.outputs.all()
    ]


def get_storage_address(asset_kind: str, key: str, field: str) -> str:
    return f"http://testserver/{asset_kind}/{key}/{field}/"


def get_permissions(owner: str, public: bool) -> dict:
    return {
        "permissions_download_public": public,
        "permissions_download_authorized_ids": [owner],
        "permissions_process_public": public,
        "permissions_process_authorized_ids": [owner],
    }


def get_log_permissions(owner: str, public: bool) -> dict:
    return {
        "logs_permission_public": public,
        "logs_permission_authorized_ids": [owner],
    }


def get_computetask_dates(status: int, creation_date: datetime.datetime) -> tuple[datetime, datetime]:
    start_date = end_date = None
    if status in (
        ComputeTask.Status.STATUS_DOING,
        ComputeTask.Status.STATUS_DONE,
        ComputeTask.Status.STATUS_FAILED,
        ComputeTask.Status.STATUS_CANCELED,
    ):
        start_date = creation_date + datetime.timedelta(hours=1)
    if status in (
        ComputeTask.Status.STATUS_DONE,
        ComputeTask.Status.STATUS_FAILED,
        ComputeTask.Status.STATUS_CANCELED,
    ):
        end_date = creation_date + datetime.timedelta(hours=2)
    return start_date, end_date


def get_computeplan_dates(status: int, creation_date: datetime.datetime) -> tuple[datetime, datetime]:
    start_date = end_date = None
    if status in (
        ComputePlan.Status.PLAN_STATUS_DOING,
        ComputePlan.Status.PLAN_STATUS_DONE,
        ComputePlan.Status.PLAN_STATUS_FAILED,
        ComputePlan.Status.PLAN_STATUS_CANCELED,
    ):
        start_date = creation_date + datetime.timedelta(hours=1)
    if status in (
        ComputePlan.Status.PLAN_STATUS_DONE,
        ComputePlan.Status.PLAN_STATUS_FAILED,
        ComputePlan.Status.PLAN_STATUS_CANCELED,
    ):
        end_date = creation_date + datetime.timedelta(hours=2)
    return start_date, end_date


def create_algo(
    inputs: list[AlgoInput] = None,
    outputs: list[AlgoInput] = None,
    key: uuid.UUID = None,
    name: str = "algo",
    metadata: dict = None,
    owner: str = DEFAULT_OWNER,
    channel: str = DEFAULT_CHANNEL,
    public: bool = False,
) -> Algo:
    if key is None:
        key = uuid.uuid4()

    algo = Algo.objects.create(
        key=key,
        name=name,
        metadata=metadata or {},
        algorithm_address=get_storage_address("algo", key, "file"),
        algorithm_checksum=DUMMY_CHECKSUM,
        description_address=get_storage_address("algo", key, "description"),
        description_checksum=DUMMY_CHECKSUM,
        creation_date=timezone.now(),
        owner=owner,
        channel=channel,
        **get_permissions(owner, public),
    )

    if inputs:
        for algo_input in inputs:
            algo_input.algo = algo
            algo_input.channel = channel
            algo_input.save()
    if outputs:
        for algo_output in outputs:
            algo_output.algo = algo
            algo_output.channel = channel
            algo_output.save()

    return algo


def create_datamanager(
    key: uuid.UUID = None,
    name: str = "datamanager",
    type: str = "Test",
    metadata: dict = None,
    owner: str = DEFAULT_OWNER,
    channel: str = DEFAULT_CHANNEL,
    public: bool = False,
) -> DataManager:
    if key is None:
        key = uuid.uuid4()
    return DataManager.objects.create(
        key=key,
        name=name,
        type=type,
        metadata=metadata or {},
        opener_address=get_storage_address("data_manager", key, "opener"),
        opener_checksum=DUMMY_CHECKSUM,
        description_address=get_storage_address("data_manager", key, "description"),
        description_checksum=DUMMY_CHECKSUM,
        creation_date=timezone.now(),
        owner=owner,
        channel=channel,
        **get_permissions(owner, public),
        **get_log_permissions(owner, public),
    )


def create_datasample(
    data_managers: list[DataManager],
    key: uuid.UUID = None,
    test_only: bool = False,
    owner: str = DEFAULT_OWNER,
    channel: str = DEFAULT_CHANNEL,
) -> DataSample:
    if key is None:
        key = uuid.uuid4()
    data_sample = DataSample.objects.create(
        key=key,
        test_only=test_only,
        creation_date=timezone.now(),
        owner=owner,
        channel=channel,
    )
    data_sample.data_managers.set(data_managers)
    data_sample.save()
    return data_sample


def create_computeplan(
    key: uuid.UUID = None,
    status: int = ComputePlan.Status.PLAN_STATUS_TODO,
    tag: str = "",
    name: str = "computeplan",
    failed_task_key: str = None,
    failed_task_category: int = None,
    metadata: dict = None,
    owner: str = DEFAULT_OWNER,
    channel: str = DEFAULT_CHANNEL,
) -> ComputePlan:
    creation_date = timezone.now()
    start_date, end_date = get_computeplan_dates(status, creation_date)
    if key is None:
        key = uuid.uuid4()
    return ComputePlan.objects.create(
        key=key,
        status=status,
        tag=tag,
        name=name,
        start_date=start_date,
        end_date=end_date,
        failed_task_key=failed_task_key,
        failed_task_category=failed_task_category,
        metadata=metadata or {},
        creation_date=creation_date,
        owner=owner,
        channel=channel,
    )


def create_computetask(
    compute_plan: ComputePlan,
    algo: Algo,
    inputs: list[ComputeTaskInput] = None,
    outputs: list[ComputeTaskOutput] = None,
    parent_tasks: list[uuid.UUID] = None,
    data_manager: DataManager = None,
    data_samples: list[uuid.UUID] = None,
    key: uuid.UUID = None,
    category: int = ComputeTask.Category.TASK_TRAIN,
    status: int = ComputeTask.Status.STATUS_TODO,
    rank: int = 1,
    worker: str = DEFAULT_WORKER,
    tag: str = "",
    error_type: int = None,
    metadata: dict = None,
    owner: str = DEFAULT_OWNER,
    channel: str = DEFAULT_CHANNEL,
    public: bool = False,
) -> ComputeTask:
    creation_date = timezone.now()
    start_date, end_date = get_computetask_dates(status, creation_date)
    if key is None:
        key = uuid.uuid4()
    compute_task = ComputeTask.objects.create(
        compute_plan=compute_plan,
        algo=algo,
        parent_tasks=parent_tasks or [],
        data_manager=data_manager,
        key=key,
        category=category,
        status=status,
        rank=rank,
        worker=worker,
        tag=tag,
        start_date=start_date,
        end_date=end_date,
        error_type=error_type,
        metadata=metadata or {},
        logs_address=get_storage_address("logs", key, "file"),
        logs_checksum=DUMMY_CHECKSUM,
        logs_owner=owner,
        creation_date=creation_date,
        owner=owner,
        channel=channel,
        **get_log_permissions(owner, public),
    )
    if data_samples:
        for order, data_sample in enumerate(data_samples):
            TaskDataSamples.objects.create(compute_task_id=key, data_sample_id=data_sample, order=order)
        compute_task.refresh_from_db()

    if inputs:
        input_kinds = {algo_input.identifier: algo_input.kind for algo_input in compute_task.algo.inputs.all()}
        for position, task_input in enumerate(inputs):
            task_input.task = compute_task
            task_input.channel = channel
            task_input.position = position
            task_input.save()
            if task_input.asset_key:
                ComputeTaskInputAsset.objects.create(
                    task_input=task_input,
                    asset_kind=input_kinds[task_input.identifier],
                    asset_key=task_input.asset_key,
                    channel=channel,
                )

    if outputs:
        for task_output in outputs:
            task_output.task = compute_task
            task_output.channel = channel
            task_output.save()

    return compute_task


def create_model(
    compute_task: ComputeTask,
    key: uuid.UUID = None,
    identifier: str = "model",
    owner: str = DEFAULT_OWNER,
    channel: str = DEFAULT_CHANNEL,
    public: bool = False,
) -> Model:
    if key is None:
        key = uuid.uuid4()
    model = Model.objects.create(
        compute_task=compute_task,
        key=key,
        model_address=get_storage_address("model", key, "file"),
        model_checksum=DUMMY_CHECKSUM,
        creation_date=timezone.now(),
        owner=owner,
        channel=channel,
        **get_permissions(owner, public),
    )
    ComputeTaskOutputAsset.objects.create(
        task_output=compute_task.outputs.get(identifier=identifier),
        asset_kind=AlgoOutput.Kind.ASSET_MODEL,
        asset_key=model.key,
        channel=channel,
    )
    for task_input in ComputeTaskInput.objects.filter(
        parent_task_key=compute_task,
        parent_task_output_identifier=identifier,
    ):
        ComputeTaskInputAsset.objects.create(
            task_input=task_input,
            asset_kind=AlgoOutput.Kind.ASSET_MODEL,
            asset_key=model.key,
            channel=channel,
        )
    return model


def create_performance(
    compute_task: ComputeTask,
    metric: Algo,
    identifier: str = "performance",
    value: float = 1.0,
    channel: str = DEFAULT_CHANNEL,
) -> Performance:
    performance = Performance.objects.create(
        value=value,
        creation_date=timezone.now(),
        channel=channel,
        metric=metric,
        compute_task=compute_task,
    )
    ComputeTaskOutputAsset.objects.create(
        task_output=compute_task.outputs.get(identifier=identifier),
        asset_kind=AlgoOutput.Kind.ASSET_PERFORMANCE,
        asset_key=f"{compute_task.key}|{metric.key}",
        channel=channel,
    )
    return performance


def create_algo_files(
    key: uuid.UUID = None,
    file: files.File = None,
    description: files.File = None,
) -> AlgoFiles:
    if key is None:
        key = uuid.uuid4()
    if file is None:
        file = files.base.ContentFile("dummy content")
    if description is None:
        description = files.base.ContentFile("dummy content")

    algo_files = AlgoFiles.objects.create(
        key=key,
        checksum=get_hash(file),
    )
    algo_files.file.save("algo", file)
    algo_files.description.save("description", description)
    return algo_files


def create_datamanager_files(
    key: uuid.UUID = None,
    name: str = "datamanager",
    opener: files.File = None,
    description: files.File = None,
) -> DataManagerFiles:
    if key is None:
        key = uuid.uuid4()
    if opener is None:
        opener = files.base.ContentFile("dummy content")
    if description is None:
        description = files.base.ContentFile("dummy content")

    data_manager_files = DataManagerFiles.objects.create(
        key=key,
        name=name,
        checksum=get_hash(opener),
    )
    data_manager_files.data_opener.save("opener", opener)
    data_manager_files.description.save("description", description)
    return data_manager_files


def create_datasample_files(
    key: uuid.UUID = None,
    file: files.File = None,
) -> DataSampleFiles:
    if key is None:
        key = uuid.uuid4()
    if file is None:
        file = files.base.ContentFile("dummy content")

    data_sample_files = DataSampleFiles.objects.create(
        key=key,
        checksum=get_hash(file),
    )
    data_sample_files.file.save("datasample", file)
    return data_sample_files


def create_model_files(
    key: uuid.UUID = None,
    file: files.File = None,
) -> ModelFiles:
    if key is None:
        key = uuid.uuid4()
    if file is None:
        file = files.base.ContentFile("dummy content")

    model_files = ModelFiles.objects.create(
        key=key,
        checksum=get_hash(file),
    )
    model_files.file.save("model", file)
    return model_files


def create_computetask_logs(
    compute_task_key: uuid.UUID,
    logs: files.File = None,
) -> ComputeTaskLogs:
    if logs is None:
        logs = files.base.ContentFile("dummy content")

    compute_task_logs = ComputeTaskLogs.objects.create(
        compute_task_key=compute_task_key,
        logs_checksum=get_hash(logs),
        creation_date=timezone.now(),
    )
    compute_task_logs.logs.save("logs", logs)
    return compute_task_logs


def create_computetask_profiling(compute_task: ComputeTask) -> TaskProfiling:
    profile = TaskProfiling.objects.create(compute_task=compute_task)
    ProfilingStep.objects.create(
        compute_task_profile=profile, step="step 1", duration=str(datetime.timedelta(seconds=10))
    )
    return profile
