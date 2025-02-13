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

class DataManager(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    KEY_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    OPENER_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    CREATION_DATE_FIELD_NUMBER: builtins.int
    LOGS_PERMISSION_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    key: builtins.str
    name: builtins.str
    owner: builtins.str
    @property
    def permissions(self) -> common_pb2.Permissions: ...
    @property
    def description(self) -> common_pb2.Addressable: ...
    @property
    def opener(self) -> common_pb2.Addressable: ...
    type: builtins.str
    @property
    def creation_date(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def logs_permission(self) -> common_pb2.Permission: ...
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        name: builtins.str = ...,
        owner: builtins.str = ...,
        permissions: common_pb2.Permissions | None = ...,
        description: common_pb2.Addressable | None = ...,
        opener: common_pb2.Addressable | None = ...,
        type: builtins.str = ...,
        creation_date: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        logs_permission: common_pb2.Permission | None = ...,
        metadata: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["creation_date", b"creation_date", "description", b"description", "logs_permission", b"logs_permission", "opener", b"opener", "permissions", b"permissions"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["creation_date", b"creation_date", "description", b"description", "key", b"key", "logs_permission", b"logs_permission", "metadata", b"metadata", "name", b"name", "opener", b"opener", "owner", b"owner", "permissions", b"permissions", "type", b"type"]) -> None: ...

global___DataManager = DataManager

class NewDataManager(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    KEY_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    NEW_PERMISSIONS_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    OPENER_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    LOGS_PERMISSION_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    key: builtins.str
    name: builtins.str
    @property
    def new_permissions(self) -> common_pb2.NewPermissions: ...
    @property
    def description(self) -> common_pb2.Addressable: ...
    @property
    def opener(self) -> common_pb2.Addressable: ...
    type: builtins.str
    @property
    def logs_permission(self) -> common_pb2.NewPermissions: ...
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        name: builtins.str = ...,
        new_permissions: common_pb2.NewPermissions | None = ...,
        description: common_pb2.Addressable | None = ...,
        opener: common_pb2.Addressable | None = ...,
        type: builtins.str = ...,
        logs_permission: common_pb2.NewPermissions | None = ...,
        metadata: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["description", b"description", "logs_permission", b"logs_permission", "new_permissions", b"new_permissions", "opener", b"opener"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "key", b"key", "logs_permission", b"logs_permission", "metadata", b"metadata", "name", b"name", "new_permissions", b"new_permissions", "opener", b"opener", "type", b"type"]) -> None: ...

global___NewDataManager = NewDataManager

class GetDataManagerParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    key: builtins.str
    def __init__(
        self,
        *,
        key: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key"]) -> None: ...

global___GetDataManagerParam = GetDataManagerParam

class QueryDataManagersParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    page_token: builtins.str
    page_size: builtins.int
    def __init__(
        self,
        *,
        page_token: builtins.str = ...,
        page_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___QueryDataManagersParam = QueryDataManagersParam

class QueryDataManagersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_MANAGERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def data_managers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DataManager]: ...
    next_page_token: builtins.str
    def __init__(
        self,
        *,
        data_managers: collections.abc.Iterable[global___DataManager] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_managers", b"data_managers", "next_page_token", b"next_page_token"]) -> None: ...

global___QueryDataManagersResponse = QueryDataManagersResponse

class UpdateDataManagerParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    key: builtins.str
    name: builtins.str
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "name", b"name"]) -> None: ...

global___UpdateDataManagerParam = UpdateDataManagerParam

class UpdateDataManagerResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___UpdateDataManagerResponse = UpdateDataManagerResponse
