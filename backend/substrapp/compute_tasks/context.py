import os
from typing import Any
from typing import Dict
from typing import List

from django.conf import settings

from orchestrator import common_pb2
from orchestrator import computetask_pb2
from substrapp.compute_tasks.algo import Algo
from substrapp.compute_tasks.compute_pod import ComputePod
from substrapp.compute_tasks.directories import SANDBOX_DIR
from substrapp.compute_tasks.directories import Directories
from substrapp.orchestrator import get_orchestrator_client

TASK_DATA_FIELD = {
    computetask_pb2.TASK_TRAIN: "train",
    computetask_pb2.TASK_PREDICT: "predict",
    computetask_pb2.TASK_TEST: "test",
    computetask_pb2.TASK_AGGREGATE: "aggregate",
    computetask_pb2.TASK_COMPOSITE: "composite",
}


class TaskResource(dict):
    """TaskResource represents a task's input or output.

    By inheriting from dict, we get JSON serialization for free
    """

    def __init__(self, id: str, value: str):
        dict.__init__(self, id=id, value=value)


class Context:
    """
    Context represents the execution context of a compute task.

    It is scoped to a single compute task. It contains all the context data which is useful during the
    whole lifetime of a compute task: channel name, task key, category, compute plan key, etc...
    """

    _channel_name: str
    _task: Dict[str, Any]
    _task_category: "computetask_pb2.ComputeTaskCategory.ValueType"
    _task_key: str
    _compute_plan_key: str
    _compute_plan_tag: str
    _compute_plan: Dict
    _in_models: List[Dict]
    _data_manager: Dict
    _directories: Directories
    _algo: Algo
    _has_chainkeys: bool
    _outputs: Dict[str, str]

    def __init__(
        self,
        channel_name: str,
        task: Dict[str, Any],
        task_category: "computetask_pb2.ComputeTaskCategory.ValueType",
        task_key: str,
        compute_plan: Dict,
        compute_plan_key: str,
        compute_plan_tag: str,
        in_models: List[Dict],
        algo: Algo,
        data_manager: Dict,
        directories: Directories,
        has_chainkeys: bool,
    ):
        self._channel_name = channel_name
        self._task = task
        self._compute_plan = compute_plan
        self._task_category = task_category
        self._task_key = task_key
        self._compute_plan_key = compute_plan_key
        self._compute_plan_tag = compute_plan_tag
        self._in_models = in_models
        self._data_manager = data_manager
        self._directories = directories
        self._has_chainkeys = has_chainkeys
        self._algo = algo
        self._outputs = {}

    @classmethod
    def from_task(cls, channel_name: str, task: dict):
        task_key = task["key"]
        compute_plan_key = task["compute_plan_key"]
        data_manager = None
        task_category = computetask_pb2.ComputeTaskCategory.Value(task["category"])

        # fetch more information from the orchestrator
        with get_orchestrator_client(channel_name) as client:
            compute_plan = client.query_compute_plan(compute_plan_key)
            in_models = client.get_computetask_input_models(task["key"])
            algo = client.query_algo(task["algo"]["key"])
            algo = Algo(channel_name, algo)

            for input in task["inputs"]:
                if _input_has_kind(input, common_pb2.ASSET_DATA_MANAGER, algo):
                    data_manager = client.query_datamanager(input["asset_key"])
                    break

        directories = Directories(compute_plan_key)

        compute_plan_tag = compute_plan["tag"]
        cp_is_tagged = True if compute_plan_tag else False
        has_chainkeys = settings.TASK["CHAINKEYS_ENABLED"] and cp_is_tagged

        return cls(
            channel_name,
            task,
            task_category,
            task_key,
            compute_plan,
            compute_plan_key,
            compute_plan_tag,
            in_models,
            algo,
            data_manager,
            directories,
            has_chainkeys,
        )

    @property
    def channel_name(self) -> str:
        return self._channel_name

    @property
    def task(self) -> Dict[str, Any]:
        return self._task

    @property
    def task_category(self) -> "computetask_pb2.ComputeTaskCategory.ValueType":
        return self._task_category

    @property
    def task_key(self) -> str:
        return self._task_key

    @property
    def task_rank(self) -> int:
        return self.task["rank"]

    @property
    def compute_plan_key(self) -> str:
        return self._compute_plan_key

    @property
    def compute_plan_tag(self) -> str:
        return self._compute_plan_tag

    @property
    def directories(self) -> Directories:
        return self._directories

    @property
    def has_chainkeys(self) -> bool:
        return self._has_chainkeys

    @property
    def in_models(self) -> List[Dict]:
        return self._in_models

    @property
    def algo(self) -> Algo:
        return self._algo

    @property
    def compute_plan(self) -> Dict:
        return self._compute_plan

    @property
    def data_manager(self) -> Dict:
        return self._data_manager

    @property
    def data_sample_keys(self) -> list[str]:
        return [
            input["asset_key"]
            for input in self.task["inputs"]
            if _input_has_kind(input, common_pb2.ASSET_DATA_SAMPLE, self.algo)
        ]

    def get_compute_pod(self, algo_key: str) -> ComputePod:
        return ComputePod(self.compute_plan_key, algo_key)

    def get_output_identifier(self, value: str) -> str:
        """return the task output identifier from output path"""
        path = os.path.relpath(value, self.directories.task_dir)
        return self._outputs[path]

    def set_outputs(self, outputs: List[TaskResource]):
        """set_outputs should be called with outputs as passed to the algo"""
        for output in outputs:
            path = os.path.relpath(output["value"], SANDBOX_DIR)
            self._outputs[path] = output["id"]


def _input_has_kind(input: dict, asset_kind: int, algo: Algo) -> bool:
    return algo.inputs[input["identifier"]]["kind"] == common_pb2.AssetKind.Name(asset_kind)
