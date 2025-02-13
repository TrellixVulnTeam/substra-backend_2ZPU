"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import common_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Model(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    COMPUTE_TASK_KEY_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    CREATION_DATE_FIELD_NUMBER: builtins.int
    key: builtins.str
    compute_task_key: builtins.str
    @property
    def address(self) -> common_pb2.Addressable: ...
    @property
    def permissions(self) -> common_pb2.Permissions: ...
    owner: builtins.str
    @property
    def creation_date(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        compute_task_key: builtins.str = ...,
        address: common_pb2.Addressable | None = ...,
        permissions: common_pb2.Permissions | None = ...,
        owner: builtins.str = ...,
        creation_date: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["address", b"address", "creation_date", b"creation_date", "permissions", b"permissions"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address", "compute_task_key", b"compute_task_key", "creation_date", b"creation_date", "key", b"key", "owner", b"owner", "permissions", b"permissions"]) -> None: ...

global___Model = Model

class NewModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    COMPUTE_TASK_KEY_FIELD_NUMBER: builtins.int
    COMPUTE_TASK_OUTPUT_IDENTIFIER_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    key: builtins.str
    compute_task_key: builtins.str
    compute_task_output_identifier: builtins.str
    @property
    def address(self) -> common_pb2.Addressable: ...
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        compute_task_key: builtins.str = ...,
        compute_task_output_identifier: builtins.str = ...,
        address: common_pb2.Addressable | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["address", b"address"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address", "compute_task_key", b"compute_task_key", "compute_task_output_identifier", b"compute_task_output_identifier", "key", b"key"]) -> None: ...

global___NewModel = NewModel

class RegisterModelsParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODELS_FIELD_NUMBER: builtins.int
    @property
    def models(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NewModel]: ...
    def __init__(
        self,
        *,
        models: collections.abc.Iterable[global___NewModel] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["models", b"models"]) -> None: ...

global___RegisterModelsParam = RegisterModelsParam

class RegisterModelsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODELS_FIELD_NUMBER: builtins.int
    @property
    def models(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Model]: ...
    def __init__(
        self,
        *,
        models: collections.abc.Iterable[global___Model] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["models", b"models"]) -> None: ...

global___RegisterModelsResponse = RegisterModelsResponse

class GetComputeTaskModelsParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMPUTE_TASK_KEY_FIELD_NUMBER: builtins.int
    compute_task_key: builtins.str
    def __init__(
        self,
        *,
        compute_task_key: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["compute_task_key", b"compute_task_key"]) -> None: ...

global___GetComputeTaskModelsParam = GetComputeTaskModelsParam

class GetComputeTaskModelsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODELS_FIELD_NUMBER: builtins.int
    @property
    def models(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Model]: ...
    def __init__(
        self,
        *,
        models: collections.abc.Iterable[global___Model] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["models", b"models"]) -> None: ...

global___GetComputeTaskModelsResponse = GetComputeTaskModelsResponse

class GetModelParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    key: builtins.str
    def __init__(
        self,
        *,
        key: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key"]) -> None: ...

global___GetModelParam = GetModelParam
