"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import common_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ModelCategory:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _ModelCategoryEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ModelCategory.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    MODEL_UNKNOWN: _ModelCategory.ValueType  # 0
    MODEL_SIMPLE: _ModelCategory.ValueType  # 1
    MODEL_HEAD: _ModelCategory.ValueType  # 2
class ModelCategory(_ModelCategory, metaclass=_ModelCategoryEnumTypeWrapper):
    pass

MODEL_UNKNOWN: ModelCategory.ValueType  # 0
MODEL_SIMPLE: ModelCategory.ValueType  # 1
MODEL_HEAD: ModelCategory.ValueType  # 2
global___ModelCategory = ModelCategory


class Model(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    CATEGORY_FIELD_NUMBER: builtins.int
    COMPUTE_TASK_KEY_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    CREATION_DATE_FIELD_NUMBER: builtins.int
    key: typing.Text
    category: global___ModelCategory.ValueType
    compute_task_key: typing.Text
    @property
    def address(self) -> common_pb2.Addressable: ...
    @property
    def permissions(self) -> common_pb2.Permissions: ...
    owner: typing.Text
    @property
    def creation_date(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        key: typing.Text = ...,
        category: global___ModelCategory.ValueType = ...,
        compute_task_key: typing.Text = ...,
        address: typing.Optional[common_pb2.Addressable] = ...,
        permissions: typing.Optional[common_pb2.Permissions] = ...,
        owner: typing.Text = ...,
        creation_date: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["address",b"address","creation_date",b"creation_date","permissions",b"permissions"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address","category",b"category","compute_task_key",b"compute_task_key","creation_date",b"creation_date","key",b"key","owner",b"owner","permissions",b"permissions"]) -> None: ...
global___Model = Model

class NewModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    CATEGORY_FIELD_NUMBER: builtins.int
    COMPUTE_TASK_KEY_FIELD_NUMBER: builtins.int
    COMPUTE_TASK_OUTPUT_IDENTIFIER_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    key: typing.Text
    category: global___ModelCategory.ValueType
    compute_task_key: typing.Text
    compute_task_output_identifier: typing.Text
    @property
    def address(self) -> common_pb2.Addressable: ...
    def __init__(self,
        *,
        key: typing.Text = ...,
        category: global___ModelCategory.ValueType = ...,
        compute_task_key: typing.Text = ...,
        compute_task_output_identifier: typing.Text = ...,
        address: typing.Optional[common_pb2.Addressable] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["address",b"address"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address","category",b"category","compute_task_key",b"compute_task_key","compute_task_output_identifier",b"compute_task_output_identifier","key",b"key"]) -> None: ...
global___NewModel = NewModel

class RegisterModelsParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODELS_FIELD_NUMBER: builtins.int
    @property
    def models(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NewModel]: ...
    def __init__(self,
        *,
        models: typing.Optional[typing.Iterable[global___NewModel]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["models",b"models"]) -> None: ...
global___RegisterModelsParam = RegisterModelsParam

class RegisterModelsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODELS_FIELD_NUMBER: builtins.int
    @property
    def models(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Model]: ...
    def __init__(self,
        *,
        models: typing.Optional[typing.Iterable[global___Model]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["models",b"models"]) -> None: ...
global___RegisterModelsResponse = RegisterModelsResponse

class GetComputeTaskModelsParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COMPUTE_TASK_KEY_FIELD_NUMBER: builtins.int
    compute_task_key: typing.Text
    def __init__(self,
        *,
        compute_task_key: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["compute_task_key",b"compute_task_key"]) -> None: ...
global___GetComputeTaskModelsParam = GetComputeTaskModelsParam

class GetComputeTaskModelsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODELS_FIELD_NUMBER: builtins.int
    @property
    def models(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Model]: ...
    def __init__(self,
        *,
        models: typing.Optional[typing.Iterable[global___Model]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["models",b"models"]) -> None: ...
global___GetComputeTaskModelsResponse = GetComputeTaskModelsResponse

class CanDisableModelParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODEL_KEY_FIELD_NUMBER: builtins.int
    model_key: typing.Text
    def __init__(self,
        *,
        model_key: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["model_key",b"model_key"]) -> None: ...
global___CanDisableModelParam = CanDisableModelParam

class CanDisableModelResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CAN_DISABLE_FIELD_NUMBER: builtins.int
    can_disable: builtins.bool
    def __init__(self,
        *,
        can_disable: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["can_disable",b"can_disable"]) -> None: ...
global___CanDisableModelResponse = CanDisableModelResponse

class DisableModelParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODEL_KEY_FIELD_NUMBER: builtins.int
    model_key: typing.Text
    def __init__(self,
        *,
        model_key: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["model_key",b"model_key"]) -> None: ...
global___DisableModelParam = DisableModelParam

class GetModelParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    key: typing.Text
    def __init__(self,
        *,
        key: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key"]) -> None: ...
global___GetModelParam = GetModelParam

class QueryModelsParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CATEGORY_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    category: global___ModelCategory.ValueType
    page_token: typing.Text
    page_size: builtins.int
    def __init__(self,
        *,
        category: global___ModelCategory.ValueType = ...,
        page_token: typing.Text = ...,
        page_size: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["category",b"category","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___QueryModelsParam = QueryModelsParam

class QueryModelsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODELS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def models(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Model]: ...
    next_page_token: typing.Text
    def __init__(self,
        *,
        models: typing.Optional[typing.Iterable[global___Model]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["models",b"models","next_page_token",b"next_page_token"]) -> None: ...
global___QueryModelsResponse = QueryModelsResponse

class DisableModelResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___DisableModelResponse = DisableModelResponse
