"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _AssetKind:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _AssetKindEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AssetKind.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ASSET_UNKNOWN: _AssetKind.ValueType  # 0
    ASSET_ORGANIZATION: _AssetKind.ValueType  # 1
    ASSET_DATA_SAMPLE: _AssetKind.ValueType  # 3
    ASSET_DATA_MANAGER: _AssetKind.ValueType  # 4
    ASSET_ALGO: _AssetKind.ValueType  # 5
    ASSET_COMPUTE_TASK: _AssetKind.ValueType  # 6
    ASSET_COMPUTE_PLAN: _AssetKind.ValueType  # 7
    ASSET_MODEL: _AssetKind.ValueType  # 8
    ASSET_PERFORMANCE: _AssetKind.ValueType  # 9
    ASSET_FAILURE_REPORT: _AssetKind.ValueType  # 10
    ASSET_COMPUTE_TASK_OUTPUT_ASSET: _AssetKind.ValueType  # 11
class AssetKind(_AssetKind, metaclass=_AssetKindEnumTypeWrapper):
    pass

ASSET_UNKNOWN: AssetKind.ValueType  # 0
ASSET_ORGANIZATION: AssetKind.ValueType  # 1
ASSET_DATA_SAMPLE: AssetKind.ValueType  # 3
ASSET_DATA_MANAGER: AssetKind.ValueType  # 4
ASSET_ALGO: AssetKind.ValueType  # 5
ASSET_COMPUTE_TASK: AssetKind.ValueType  # 6
ASSET_COMPUTE_PLAN: AssetKind.ValueType  # 7
ASSET_MODEL: AssetKind.ValueType  # 8
ASSET_PERFORMANCE: AssetKind.ValueType  # 9
ASSET_FAILURE_REPORT: AssetKind.ValueType  # 10
ASSET_COMPUTE_TASK_OUTPUT_ASSET: AssetKind.ValueType  # 11
global___AssetKind = AssetKind


class _SortOrder:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _SortOrderEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SortOrder.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNSPECIFIED: _SortOrder.ValueType  # 0
    ASCENDING: _SortOrder.ValueType  # 1
    DESCENDING: _SortOrder.ValueType  # 2
class SortOrder(_SortOrder, metaclass=_SortOrderEnumTypeWrapper):
    pass

UNSPECIFIED: SortOrder.ValueType  # 0
ASCENDING: SortOrder.ValueType  # 1
DESCENDING: SortOrder.ValueType  # 2
global___SortOrder = SortOrder


class Addressable(google.protobuf.message.Message):
    """Addressable references an asset on the network.
    It contains both its address (backend URL) and checksum.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CHECKSUM_FIELD_NUMBER: builtins.int
    STORAGE_ADDRESS_FIELD_NUMBER: builtins.int
    checksum: typing.Text
    storage_address: typing.Text
    def __init__(self,
        *,
        checksum: typing.Text = ...,
        storage_address: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["checksum",b"checksum","storage_address",b"storage_address"]) -> None: ...
global___Addressable = Addressable

class Permissions(google.protobuf.message.Message):
    """Permissions for an asset, each key is an action"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROCESS_FIELD_NUMBER: builtins.int
    DOWNLOAD_FIELD_NUMBER: builtins.int
    @property
    def process(self) -> global___Permission: ...
    @property
    def download(self) -> global___Permission: ...
    def __init__(self,
        *,
        process: typing.Optional[global___Permission] = ...,
        download: typing.Optional[global___Permission] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["download",b"download","process",b"process"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["download",b"download","process",b"process"]) -> None: ...
global___Permissions = Permissions

class Permission(google.protobuf.message.Message):
    """Permission represents the permission for a single action"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PUBLIC_FIELD_NUMBER: builtins.int
    AUTHORIZED_IDS_FIELD_NUMBER: builtins.int
    public: builtins.bool
    @property
    def authorized_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        public: builtins.bool = ...,
        authorized_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["authorized_ids",b"authorized_ids","public",b"public"]) -> None: ...
global___Permission = Permission

class NewPermissions(google.protobuf.message.Message):
    """NewPermissions is used to create a new permission set.
    This will be transformed in a full Permissions structure on registration.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PUBLIC_FIELD_NUMBER: builtins.int
    AUTHORIZED_IDS_FIELD_NUMBER: builtins.int
    public: builtins.bool
    @property
    def authorized_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        public: builtins.bool = ...,
        authorized_ids: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["authorized_ids",b"authorized_ids","public",b"public"]) -> None: ...
global___NewPermissions = NewPermissions
