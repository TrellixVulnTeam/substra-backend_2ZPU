"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import algo_pb2
import builtins
import common_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _ComputeTaskCategory:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ComputeTaskCategoryEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ComputeTaskCategory.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    TASK_UNKNOWN: ComputeTaskCategory.ValueType = ...  # 0
    TASK_TRAIN: ComputeTaskCategory.ValueType = ...  # 1
    TASK_AGGREGATE: ComputeTaskCategory.ValueType = ...  # 2
    TASK_COMPOSITE: ComputeTaskCategory.ValueType = ...  # 3
    TASK_TEST: ComputeTaskCategory.ValueType = ...  # 4
class ComputeTaskCategory(_ComputeTaskCategory, metaclass=_ComputeTaskCategoryEnumTypeWrapper):
    pass

TASK_UNKNOWN: ComputeTaskCategory.ValueType = ...  # 0
TASK_TRAIN: ComputeTaskCategory.ValueType = ...  # 1
TASK_AGGREGATE: ComputeTaskCategory.ValueType = ...  # 2
TASK_COMPOSITE: ComputeTaskCategory.ValueType = ...  # 3
TASK_TEST: ComputeTaskCategory.ValueType = ...  # 4
global___ComputeTaskCategory = ComputeTaskCategory


class _ComputeTaskStatus:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ComputeTaskStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ComputeTaskStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    STATUS_UNKNOWN: ComputeTaskStatus.ValueType = ...  # 0
    STATUS_WAITING: ComputeTaskStatus.ValueType = ...  # 1
    STATUS_TODO: ComputeTaskStatus.ValueType = ...  # 2
    STATUS_DOING: ComputeTaskStatus.ValueType = ...  # 3
    STATUS_DONE: ComputeTaskStatus.ValueType = ...  # 4
    STATUS_CANCELED: ComputeTaskStatus.ValueType = ...  # 5
    STATUS_FAILED: ComputeTaskStatus.ValueType = ...  # 6
class ComputeTaskStatus(_ComputeTaskStatus, metaclass=_ComputeTaskStatusEnumTypeWrapper):
    pass

STATUS_UNKNOWN: ComputeTaskStatus.ValueType = ...  # 0
STATUS_WAITING: ComputeTaskStatus.ValueType = ...  # 1
STATUS_TODO: ComputeTaskStatus.ValueType = ...  # 2
STATUS_DOING: ComputeTaskStatus.ValueType = ...  # 3
STATUS_DONE: ComputeTaskStatus.ValueType = ...  # 4
STATUS_CANCELED: ComputeTaskStatus.ValueType = ...  # 5
STATUS_FAILED: ComputeTaskStatus.ValueType = ...  # 6
global___ComputeTaskStatus = ComputeTaskStatus


class _ComputeTaskAction:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ComputeTaskActionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ComputeTaskAction.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    TASK_ACTION_UNKNOWN: ComputeTaskAction.ValueType = ...  # 0
    TASK_ACTION_DOING: ComputeTaskAction.ValueType = ...  # 1
    TASK_ACTION_CANCELED: ComputeTaskAction.ValueType = ...  # 2
    TASK_ACTION_FAILED: ComputeTaskAction.ValueType = ...  # 3
class ComputeTaskAction(_ComputeTaskAction, metaclass=_ComputeTaskActionEnumTypeWrapper):
    pass

TASK_ACTION_UNKNOWN: ComputeTaskAction.ValueType = ...  # 0
TASK_ACTION_DOING: ComputeTaskAction.ValueType = ...  # 1
TASK_ACTION_CANCELED: ComputeTaskAction.ValueType = ...  # 2
TASK_ACTION_FAILED: ComputeTaskAction.ValueType = ...  # 3
global___ComputeTaskAction = ComputeTaskAction


class ComputeTask(google.protobuf.message.Message):
    """ComputeTask is a computation step in a ComputePlan.
    It was previously called XXXtuple: Traintuple, CompositeTraintuple, etc
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    KEY_FIELD_NUMBER: builtins.int
    CATEGORY_FIELD_NUMBER: builtins.int
    ALGO_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    COMPUTE_PLAN_KEY_FIELD_NUMBER: builtins.int
    PARENT_TASK_KEYS_FIELD_NUMBER: builtins.int
    RANK_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    WORKER_FIELD_NUMBER: builtins.int
    CREATION_DATE_FIELD_NUMBER: builtins.int
    LOGS_PERMISSION_FIELD_NUMBER: builtins.int
    TEST_FIELD_NUMBER: builtins.int
    TRAIN_FIELD_NUMBER: builtins.int
    COMPOSITE_FIELD_NUMBER: builtins.int
    AGGREGATE_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    key: typing.Text = ...
    category: global___ComputeTaskCategory.ValueType = ...
    @property
    def algo(self) -> algo_pb2.Algo: ...
    owner: typing.Text = ...
    compute_plan_key: typing.Text = ...
    @property
    def parent_task_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Keys of parent ComputeTasks"""
        pass
    rank: builtins.int = ...
    status: global___ComputeTaskStatus.ValueType = ...
    """mutable"""

    worker: typing.Text = ...
    @property
    def creation_date(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def logs_permission(self) -> common_pb2.Permission: ...
    @property
    def test(self) -> global___TestTaskData: ...
    @property
    def train(self) -> global___TrainTaskData: ...
    @property
    def composite(self) -> global___CompositeTrainTaskData: ...
    @property
    def aggregate(self) -> global___AggregateTrainTaskData: ...
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    def __init__(self,
        *,
        key : typing.Text = ...,
        category : global___ComputeTaskCategory.ValueType = ...,
        algo : typing.Optional[algo_pb2.Algo] = ...,
        owner : typing.Text = ...,
        compute_plan_key : typing.Text = ...,
        parent_task_keys : typing.Optional[typing.Iterable[typing.Text]] = ...,
        rank : builtins.int = ...,
        status : global___ComputeTaskStatus.ValueType = ...,
        worker : typing.Text = ...,
        creation_date : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        logs_permission : typing.Optional[common_pb2.Permission] = ...,
        test : typing.Optional[global___TestTaskData] = ...,
        train : typing.Optional[global___TrainTaskData] = ...,
        composite : typing.Optional[global___CompositeTrainTaskData] = ...,
        aggregate : typing.Optional[global___AggregateTrainTaskData] = ...,
        metadata : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["aggregate",b"aggregate","algo",b"algo","composite",b"composite","creation_date",b"creation_date","data",b"data","logs_permission",b"logs_permission","test",b"test","train",b"train"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["aggregate",b"aggregate","algo",b"algo","category",b"category","composite",b"composite","compute_plan_key",b"compute_plan_key","creation_date",b"creation_date","data",b"data","key",b"key","logs_permission",b"logs_permission","metadata",b"metadata","owner",b"owner","parent_task_keys",b"parent_task_keys","rank",b"rank","status",b"status","test",b"test","train",b"train","worker",b"worker"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["data",b"data"]) -> typing.Optional[typing_extensions.Literal["test","train","composite","aggregate"]]: ...
global___ComputeTask = ComputeTask

class NewComputeTask(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    KEY_FIELD_NUMBER: builtins.int
    CATEGORY_FIELD_NUMBER: builtins.int
    ALGO_KEY_FIELD_NUMBER: builtins.int
    COMPUTE_PLAN_KEY_FIELD_NUMBER: builtins.int
    PARENT_TASK_KEYS_FIELD_NUMBER: builtins.int
    TEST_FIELD_NUMBER: builtins.int
    TRAIN_FIELD_NUMBER: builtins.int
    COMPOSITE_FIELD_NUMBER: builtins.int
    AGGREGATE_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    key: typing.Text = ...
    category: global___ComputeTaskCategory.ValueType = ...
    algo_key: typing.Text = ...
    compute_plan_key: typing.Text = ...
    @property
    def parent_task_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """Keys of parent ComputeTasks"""
        pass
    @property
    def test(self) -> global___NewTestTaskData: ...
    @property
    def train(self) -> global___NewTrainTaskData: ...
    @property
    def composite(self) -> global___NewCompositeTrainTaskData: ...
    @property
    def aggregate(self) -> global___NewAggregateTrainTaskData: ...
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    def __init__(self,
        *,
        key : typing.Text = ...,
        category : global___ComputeTaskCategory.ValueType = ...,
        algo_key : typing.Text = ...,
        compute_plan_key : typing.Text = ...,
        parent_task_keys : typing.Optional[typing.Iterable[typing.Text]] = ...,
        test : typing.Optional[global___NewTestTaskData] = ...,
        train : typing.Optional[global___NewTrainTaskData] = ...,
        composite : typing.Optional[global___NewCompositeTrainTaskData] = ...,
        aggregate : typing.Optional[global___NewAggregateTrainTaskData] = ...,
        metadata : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["aggregate",b"aggregate","composite",b"composite","data",b"data","test",b"test","train",b"train"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["aggregate",b"aggregate","algo_key",b"algo_key","category",b"category","composite",b"composite","compute_plan_key",b"compute_plan_key","data",b"data","key",b"key","metadata",b"metadata","parent_task_keys",b"parent_task_keys","test",b"test","train",b"train"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["data",b"data"]) -> typing.Optional[typing_extensions.Literal["test","train","composite","aggregate"]]: ...
global___NewComputeTask = NewComputeTask

class TrainTaskData(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_MANAGER_KEY_FIELD_NUMBER: builtins.int
    DATA_SAMPLE_KEYS_FIELD_NUMBER: builtins.int
    MODEL_PERMISSIONS_FIELD_NUMBER: builtins.int
    data_manager_key: typing.Text = ...
    @property
    def data_sample_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def model_permissions(self) -> common_pb2.Permissions: ...
    def __init__(self,
        *,
        data_manager_key : typing.Text = ...,
        data_sample_keys : typing.Optional[typing.Iterable[typing.Text]] = ...,
        model_permissions : typing.Optional[common_pb2.Permissions] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["model_permissions",b"model_permissions"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_manager_key",b"data_manager_key","data_sample_keys",b"data_sample_keys","model_permissions",b"model_permissions"]) -> None: ...
global___TrainTaskData = TrainTaskData

class NewTrainTaskData(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_MANAGER_KEY_FIELD_NUMBER: builtins.int
    DATA_SAMPLE_KEYS_FIELD_NUMBER: builtins.int
    data_manager_key: typing.Text = ...
    @property
    def data_sample_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        data_manager_key : typing.Text = ...,
        data_sample_keys : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_manager_key",b"data_manager_key","data_sample_keys",b"data_sample_keys"]) -> None: ...
global___NewTrainTaskData = NewTrainTaskData

class TestTaskData(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_MANAGER_KEY_FIELD_NUMBER: builtins.int
    DATA_SAMPLE_KEYS_FIELD_NUMBER: builtins.int
    METRIC_KEYS_FIELD_NUMBER: builtins.int
    data_manager_key: typing.Text = ...
    @property
    def data_sample_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def metric_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        data_manager_key : typing.Text = ...,
        data_sample_keys : typing.Optional[typing.Iterable[typing.Text]] = ...,
        metric_keys : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_manager_key",b"data_manager_key","data_sample_keys",b"data_sample_keys","metric_keys",b"metric_keys"]) -> None: ...
global___TestTaskData = TestTaskData

class NewTestTaskData(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_MANAGER_KEY_FIELD_NUMBER: builtins.int
    DATA_SAMPLE_KEYS_FIELD_NUMBER: builtins.int
    METRIC_KEYS_FIELD_NUMBER: builtins.int
    data_manager_key: typing.Text = ...
    @property
    def data_sample_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def metric_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        data_manager_key : typing.Text = ...,
        data_sample_keys : typing.Optional[typing.Iterable[typing.Text]] = ...,
        metric_keys : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_manager_key",b"data_manager_key","data_sample_keys",b"data_sample_keys","metric_keys",b"metric_keys"]) -> None: ...
global___NewTestTaskData = NewTestTaskData

class CompositeTrainTaskData(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_MANAGER_KEY_FIELD_NUMBER: builtins.int
    DATA_SAMPLE_KEYS_FIELD_NUMBER: builtins.int
    HEAD_PERMISSIONS_FIELD_NUMBER: builtins.int
    TRUNK_PERMISSIONS_FIELD_NUMBER: builtins.int
    data_manager_key: typing.Text = ...
    @property
    def data_sample_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def head_permissions(self) -> common_pb2.Permissions: ...
    @property
    def trunk_permissions(self) -> common_pb2.Permissions: ...
    def __init__(self,
        *,
        data_manager_key : typing.Text = ...,
        data_sample_keys : typing.Optional[typing.Iterable[typing.Text]] = ...,
        head_permissions : typing.Optional[common_pb2.Permissions] = ...,
        trunk_permissions : typing.Optional[common_pb2.Permissions] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["head_permissions",b"head_permissions","trunk_permissions",b"trunk_permissions"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_manager_key",b"data_manager_key","data_sample_keys",b"data_sample_keys","head_permissions",b"head_permissions","trunk_permissions",b"trunk_permissions"]) -> None: ...
global___CompositeTrainTaskData = CompositeTrainTaskData

class NewCompositeTrainTaskData(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATA_MANAGER_KEY_FIELD_NUMBER: builtins.int
    DATA_SAMPLE_KEYS_FIELD_NUMBER: builtins.int
    TRUNK_PERMISSIONS_FIELD_NUMBER: builtins.int
    data_manager_key: typing.Text = ...
    @property
    def data_sample_keys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def trunk_permissions(self) -> common_pb2.NewPermissions: ...
    def __init__(self,
        *,
        data_manager_key : typing.Text = ...,
        data_sample_keys : typing.Optional[typing.Iterable[typing.Text]] = ...,
        trunk_permissions : typing.Optional[common_pb2.NewPermissions] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["trunk_permissions",b"trunk_permissions"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_manager_key",b"data_manager_key","data_sample_keys",b"data_sample_keys","trunk_permissions",b"trunk_permissions"]) -> None: ...
global___NewCompositeTrainTaskData = NewCompositeTrainTaskData

class AggregateTrainTaskData(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MODEL_PERMISSIONS_FIELD_NUMBER: builtins.int
    @property
    def model_permissions(self) -> common_pb2.Permissions: ...
    def __init__(self,
        *,
        model_permissions : typing.Optional[common_pb2.Permissions] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["model_permissions",b"model_permissions"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["model_permissions",b"model_permissions"]) -> None: ...
global___AggregateTrainTaskData = AggregateTrainTaskData

class NewAggregateTrainTaskData(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WORKER_FIELD_NUMBER: builtins.int
    worker: typing.Text = ...
    def __init__(self,
        *,
        worker : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["worker",b"worker"]) -> None: ...
global___NewAggregateTrainTaskData = NewAggregateTrainTaskData

class RegisterTasksParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TASKS_FIELD_NUMBER: builtins.int
    @property
    def tasks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NewComputeTask]: ...
    def __init__(self,
        *,
        tasks : typing.Optional[typing.Iterable[global___NewComputeTask]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["tasks",b"tasks"]) -> None: ...
global___RegisterTasksParam = RegisterTasksParam

class RegisterTasksResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TASKS_FIELD_NUMBER: builtins.int
    @property
    def tasks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ComputeTask]: ...
    def __init__(self,
        *,
        tasks : typing.Optional[typing.Iterable[global___ComputeTask]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["tasks",b"tasks"]) -> None: ...
global___RegisterTasksResponse = RegisterTasksResponse

class TaskQueryFilter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    WORKER_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    CATEGORY_FIELD_NUMBER: builtins.int
    COMPUTE_PLAN_KEY_FIELD_NUMBER: builtins.int
    ALGO_KEY_FIELD_NUMBER: builtins.int
    worker: typing.Text = ...
    status: global___ComputeTaskStatus.ValueType = ...
    category: global___ComputeTaskCategory.ValueType = ...
    compute_plan_key: typing.Text = ...
    algo_key: typing.Text = ...
    def __init__(self,
        *,
        worker : typing.Text = ...,
        status : global___ComputeTaskStatus.ValueType = ...,
        category : global___ComputeTaskCategory.ValueType = ...,
        compute_plan_key : typing.Text = ...,
        algo_key : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["algo_key",b"algo_key","category",b"category","compute_plan_key",b"compute_plan_key","status",b"status","worker",b"worker"]) -> None: ...
global___TaskQueryFilter = TaskQueryFilter

class QueryTasksParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    page_token: typing.Text = ...
    page_size: builtins.int = ...
    @property
    def filter(self) -> global___TaskQueryFilter: ...
    def __init__(self,
        *,
        page_token : typing.Text = ...,
        page_size : builtins.int = ...,
        filter : typing.Optional[global___TaskQueryFilter] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter",b"filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___QueryTasksParam = QueryTasksParam

class QueryTasksResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TASKS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def tasks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ComputeTask]: ...
    next_page_token: typing.Text = ...
    def __init__(self,
        *,
        tasks : typing.Optional[typing.Iterable[global___ComputeTask]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token",b"next_page_token","tasks",b"tasks"]) -> None: ...
global___QueryTasksResponse = QueryTasksResponse

class GetTaskParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_FIELD_NUMBER: builtins.int
    key: typing.Text = ...
    def __init__(self,
        *,
        key : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key"]) -> None: ...
global___GetTaskParam = GetTaskParam

class ApplyTaskActionParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COMPUTE_TASK_KEY_FIELD_NUMBER: builtins.int
    ACTION_FIELD_NUMBER: builtins.int
    LOG_FIELD_NUMBER: builtins.int
    compute_task_key: typing.Text = ...
    action: global___ComputeTaskAction.ValueType = ...
    log: typing.Text = ...
    def __init__(self,
        *,
        compute_task_key : typing.Text = ...,
        action : global___ComputeTaskAction.ValueType = ...,
        log : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["action",b"action","compute_task_key",b"compute_task_key","log",b"log"]) -> None: ...
global___ApplyTaskActionParam = ApplyTaskActionParam

class ApplyTaskActionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___ApplyTaskActionResponse = ApplyTaskActionResponse
