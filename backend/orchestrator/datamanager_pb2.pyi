"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import common_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class DataManager(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

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
    key: typing.Text
    name: typing.Text
    owner: typing.Text
    @property
    def permissions(self) -> common_pb2.Permissions: ...
    @property
    def description(self) -> common_pb2.Addressable: ...
    @property
    def opener(self) -> common_pb2.Addressable: ...
    type: typing.Text
    @property
    def creation_date(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def logs_permission(self) -> common_pb2.Permission: ...
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    def __init__(self,
        *,
        key: typing.Text = ...,
        name: typing.Text = ...,
        owner: typing.Text = ...,
        permissions: typing.Optional[common_pb2.Permissions] = ...,
        description: typing.Optional[common_pb2.Addressable] = ...,
        opener: typing.Optional[common_pb2.Addressable] = ...,
        type: typing.Text = ...,
        creation_date: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        logs_permission: typing.Optional[common_pb2.Permission] = ...,
        metadata: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["creation_date",b"creation_date","description",b"description","logs_permission",b"logs_permission","opener",b"opener","permissions",b"permissions"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["creation_date",b"creation_date","description",b"description","key",b"key","logs_permission",b"logs_permission","metadata",b"metadata","name",b"name","opener",b"opener","owner",b"owner","permissions",b"permissions","type",b"type"]) -> None: ...
global___DataManager = DataManager

class NewDataManager(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    KEY_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    NEW_PERMISSIONS_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    OPENER_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    LOGS_PERMISSION_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    key: typing.Text
    name: typing.Text
    @property
    def new_permissions(self) -> common_pb2.NewPermissions: ...
    @property
    def description(self) -> common_pb2.Addressable: ...
    @property
    def opener(self) -> common_pb2.Addressable: ...
    type: typing.Text
    @property
    def logs_permission(self) -> common_pb2.NewPermissions: ...
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    def __init__(self,
        *,
        key: typing.Text = ...,
        name: typing.Text = ...,
        new_permissions: typing.Optional[common_pb2.NewPermissions] = ...,
        description: typing.Optional[common_pb2.Addressable] = ...,
        opener: typing.Optional[common_pb2.Addressable] = ...,
        type: typing.Text = ...,
        logs_permission: typing.Optional[common_pb2.NewPermissions] = ...,
        metadata: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["description",b"description","logs_permission",b"logs_permission","new_permissions",b"new_permissions","opener",b"opener"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","key",b"key","logs_permission",b"logs_permission","metadata",b"metadata","name",b"name","new_permissions",b"new_permissions","opener",b"opener","type",b"type"]) -> None: ...
global___NewDataManager = NewDataManager

class GetDataManagerParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    key: typing.Text
    def __init__(self,
        *,
        key: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key"]) -> None: ...
global___GetDataManagerParam = GetDataManagerParam

class QueryDataManagersParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    page_token: typing.Text
    page_size: builtins.int
    def __init__(self,
        *,
        page_token: typing.Text = ...,
        page_size: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___QueryDataManagersParam = QueryDataManagersParam

class QueryDataManagersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_MANAGERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def data_managers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DataManager]: ...
    next_page_token: typing.Text
    def __init__(self,
        *,
        data_managers: typing.Optional[typing.Iterable[global___DataManager]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_managers",b"data_managers","next_page_token",b"next_page_token"]) -> None: ...
global___QueryDataManagersResponse = QueryDataManagersResponse

class UpdateDataManagerParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    key: typing.Text
    name: typing.Text
    def __init__(self,
        *,
        key: typing.Text = ...,
        name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key","name",b"name"]) -> None: ...
global___UpdateDataManagerParam = UpdateDataManagerParam

class UpdateDataManagerResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___UpdateDataManagerResponse = UpdateDataManagerResponse
