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

class _AlgoCategory:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _AlgoCategoryEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AlgoCategory.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ALGO_UNKNOWN: _AlgoCategory.ValueType  # 0
    ALGO_SIMPLE: _AlgoCategory.ValueType  # 1
    ALGO_AGGREGATE: _AlgoCategory.ValueType  # 2
    ALGO_COMPOSITE: _AlgoCategory.ValueType  # 3
    ALGO_METRIC: _AlgoCategory.ValueType  # 4
class AlgoCategory(_AlgoCategory, metaclass=_AlgoCategoryEnumTypeWrapper):
    pass

ALGO_UNKNOWN: AlgoCategory.ValueType  # 0
ALGO_SIMPLE: AlgoCategory.ValueType  # 1
ALGO_AGGREGATE: AlgoCategory.ValueType  # 2
ALGO_COMPOSITE: AlgoCategory.ValueType  # 3
ALGO_METRIC: AlgoCategory.ValueType  # 4
global___AlgoCategory = AlgoCategory


class Algo(google.protobuf.message.Message):
    """Algo represents the algorithm code which will be used
    to produce or test a model.
    """
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
    CATEGORY_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    ALGORITHM_FIELD_NUMBER: builtins.int
    PERMISSIONS_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    CREATION_DATE_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    key: typing.Text
    name: typing.Text
    category: global___AlgoCategory.ValueType
    @property
    def description(self) -> common_pb2.Addressable: ...
    @property
    def algorithm(self) -> common_pb2.Addressable: ...
    @property
    def permissions(self) -> common_pb2.Permissions: ...
    owner: typing.Text
    @property
    def creation_date(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    def __init__(self,
        *,
        key: typing.Text = ...,
        name: typing.Text = ...,
        category: global___AlgoCategory.ValueType = ...,
        description: typing.Optional[common_pb2.Addressable] = ...,
        algorithm: typing.Optional[common_pb2.Addressable] = ...,
        permissions: typing.Optional[common_pb2.Permissions] = ...,
        owner: typing.Text = ...,
        creation_date: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        metadata: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["algorithm",b"algorithm","creation_date",b"creation_date","description",b"description","permissions",b"permissions"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["algorithm",b"algorithm","category",b"category","creation_date",b"creation_date","description",b"description","key",b"key","metadata",b"metadata","name",b"name","owner",b"owner","permissions",b"permissions"]) -> None: ...
global___Algo = Algo

class NewAlgo(google.protobuf.message.Message):
    """NewAlgo is used to register an Algo.
    It will be processed into an Algo.
    """
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
    CATEGORY_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    ALGORITHM_FIELD_NUMBER: builtins.int
    NEW_PERMISSIONS_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    key: typing.Text
    name: typing.Text
    category: global___AlgoCategory.ValueType
    @property
    def description(self) -> common_pb2.Addressable: ...
    @property
    def algorithm(self) -> common_pb2.Addressable: ...
    @property
    def new_permissions(self) -> common_pb2.NewPermissions: ...
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    def __init__(self,
        *,
        key: typing.Text = ...,
        name: typing.Text = ...,
        category: global___AlgoCategory.ValueType = ...,
        description: typing.Optional[common_pb2.Addressable] = ...,
        algorithm: typing.Optional[common_pb2.Addressable] = ...,
        new_permissions: typing.Optional[common_pb2.NewPermissions] = ...,
        metadata: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["algorithm",b"algorithm","description",b"description","new_permissions",b"new_permissions"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["algorithm",b"algorithm","category",b"category","description",b"description","key",b"key","metadata",b"metadata","name",b"name","new_permissions",b"new_permissions"]) -> None: ...
global___NewAlgo = NewAlgo

class GetAlgoParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    key: typing.Text
    def __init__(self,
        *,
        key: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key"]) -> None: ...
global___GetAlgoParam = GetAlgoParam

class QueryAlgosResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ALGOS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def Algos(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Algo]: ...
    next_page_token: typing.Text
    def __init__(self,
        *,
        Algos: typing.Optional[typing.Iterable[global___Algo]] = ...,
        next_page_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["Algos",b"Algos","next_page_token",b"next_page_token"]) -> None: ...
global___QueryAlgosResponse = QueryAlgosResponse

class AlgoQueryFilter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CATEGORIES_FIELD_NUMBER: builtins.int
    COMPUTE_PLAN_KEY_FIELD_NUMBER: builtins.int
    @property
    def categories(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___AlgoCategory.ValueType]: ...
    compute_plan_key: typing.Text
    def __init__(self,
        *,
        categories: typing.Optional[typing.Iterable[global___AlgoCategory.ValueType]] = ...,
        compute_plan_key: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["categories",b"categories","compute_plan_key",b"compute_plan_key"]) -> None: ...
global___AlgoQueryFilter = AlgoQueryFilter

class QueryAlgosParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    page_token: typing.Text
    page_size: builtins.int
    @property
    def filter(self) -> global___AlgoQueryFilter: ...
    def __init__(self,
        *,
        page_token: typing.Text = ...,
        page_size: builtins.int = ...,
        filter: typing.Optional[global___AlgoQueryFilter] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter",b"filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token"]) -> None: ...
global___QueryAlgosParam = QueryAlgosParam
