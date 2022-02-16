# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='model.proto',
  package='orchestrator',
  syntax='proto3',
  serialized_options=b'Z\'github.com/owkin/orchestrator/lib/asset',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bmodel.proto\x12\x0corchestrator\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0c\x63ommon.proto\"\xfb\x01\n\x05Model\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x1b.orchestrator.ModelCategory\x12\x18\n\x10\x63ompute_task_key\x18\x03 \x01(\t\x12*\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x19.orchestrator.Addressable\x12.\n\x0bpermissions\x18\x05 \x01(\x0b\x32\x19.orchestrator.Permissions\x12\r\n\x05owner\x18\x06 \x01(\t\x12\x31\n\rcreation_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x8c\x01\n\x08NewModel\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x1b.orchestrator.ModelCategory\x12\x18\n\x10\x63ompute_task_key\x18\x03 \x01(\t\x12*\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x19.orchestrator.Addressable\"=\n\x13RegisterModelsParam\x12&\n\x06models\x18\x01 \x03(\x0b\x32\x16.orchestrator.NewModel\"=\n\x16RegisterModelsResponse\x12#\n\x06models\x18\x01 \x03(\x0b\x32\x13.orchestrator.Model\"5\n\x19GetComputeTaskModelsParam\x12\x18\n\x10\x63ompute_task_key\x18\x01 \x01(\t\"C\n\x1cGetComputeTaskModelsResponse\x12#\n\x06models\x18\x01 \x03(\x0b\x32\x13.orchestrator.Model\")\n\x14\x43\x61nDisableModelParam\x12\x11\n\tmodel_key\x18\x01 \x01(\t\".\n\x17\x43\x61nDisableModelResponse\x12\x13\n\x0b\x63\x61n_disable\x18\x01 \x01(\x08\"&\n\x11\x44isableModelParam\x12\x11\n\tmodel_key\x18\x01 \x01(\t\"\x1c\n\rGetModelParam\x12\x0b\n\x03key\x18\x01 \x01(\t\"h\n\x10QueryModelsParam\x12-\n\x08\x63\x61tegory\x18\x01 \x01(\x0e\x32\x1b.orchestrator.ModelCategory\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\r\"S\n\x13QueryModelsResponse\x12#\n\x06models\x18\x01 \x03(\x0b\x32\x13.orchestrator.Model\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x16\n\x14\x44isableModelResponse*D\n\rModelCategory\x12\x11\n\rMODEL_UNKNOWN\x10\x00\x12\x10\n\x0cMODEL_SIMPLE\x10\x01\x12\x0e\n\nMODEL_HEAD\x10\x02\x32\xd4\x05\n\x0cModelService\x12\x41\n\rRegisterModel\x12\x16.orchestrator.NewModel\x1a\x13.orchestrator.Model\"\x03\x88\x02\x01\x12Y\n\x0eRegisterModels\x12!.orchestrator.RegisterModelsParam\x1a$.orchestrator.RegisterModelsResponse\x12<\n\x08GetModel\x12\x1b.orchestrator.GetModelParam\x1a\x13.orchestrator.Model\x12P\n\x0bQueryModels\x12\x1e.orchestrator.QueryModelsParam\x1a!.orchestrator.QueryModelsResponse\x12q\n\x1aGetComputeTaskOutputModels\x12\'.orchestrator.GetComputeTaskModelsParam\x1a*.orchestrator.GetComputeTaskModelsResponse\x12p\n\x19GetComputeTaskInputModels\x12\'.orchestrator.GetComputeTaskModelsParam\x1a*.orchestrator.GetComputeTaskModelsResponse\x12\\\n\x0f\x43\x61nDisableModel\x12\".orchestrator.CanDisableModelParam\x1a%.orchestrator.CanDisableModelResponse\x12S\n\x0c\x44isableModel\x12\x1f.orchestrator.DisableModelParam\x1a\".orchestrator.DisableModelResponseB)Z\'github.com/owkin/orchestrator/lib/assetb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,])

_MODELCATEGORY = _descriptor.EnumDescriptor(
  name='ModelCategory',
  full_name='orchestrator.ModelCategory',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MODEL_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MODEL_SIMPLE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MODEL_HEAD', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1099,
  serialized_end=1167,
)
_sym_db.RegisterEnumDescriptor(_MODELCATEGORY)

ModelCategory = enum_type_wrapper.EnumTypeWrapper(_MODELCATEGORY)
MODEL_UNKNOWN = 0
MODEL_SIMPLE = 1
MODEL_HEAD = 2



_MODEL = _descriptor.Descriptor(
  name='Model',
  full_name='orchestrator.Model',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.Model.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='orchestrator.Model.category', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compute_task_key', full_name='orchestrator.Model.compute_task_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='orchestrator.Model.address', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='orchestrator.Model.permissions', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='orchestrator.Model.owner', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_date', full_name='orchestrator.Model.creation_date', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=328,
)


_NEWMODEL = _descriptor.Descriptor(
  name='NewModel',
  full_name='orchestrator.NewModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.NewModel.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='orchestrator.NewModel.category', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compute_task_key', full_name='orchestrator.NewModel.compute_task_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='orchestrator.NewModel.address', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=331,
  serialized_end=471,
)


_REGISTERMODELSPARAM = _descriptor.Descriptor(
  name='RegisterModelsParam',
  full_name='orchestrator.RegisterModelsParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='models', full_name='orchestrator.RegisterModelsParam.models', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=473,
  serialized_end=534,
)


_REGISTERMODELSRESPONSE = _descriptor.Descriptor(
  name='RegisterModelsResponse',
  full_name='orchestrator.RegisterModelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='models', full_name='orchestrator.RegisterModelsResponse.models', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=536,
  serialized_end=597,
)


_GETCOMPUTETASKMODELSPARAM = _descriptor.Descriptor(
  name='GetComputeTaskModelsParam',
  full_name='orchestrator.GetComputeTaskModelsParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='compute_task_key', full_name='orchestrator.GetComputeTaskModelsParam.compute_task_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=599,
  serialized_end=652,
)


_GETCOMPUTETASKMODELSRESPONSE = _descriptor.Descriptor(
  name='GetComputeTaskModelsResponse',
  full_name='orchestrator.GetComputeTaskModelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='models', full_name='orchestrator.GetComputeTaskModelsResponse.models', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=654,
  serialized_end=721,
)


_CANDISABLEMODELPARAM = _descriptor.Descriptor(
  name='CanDisableModelParam',
  full_name='orchestrator.CanDisableModelParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_key', full_name='orchestrator.CanDisableModelParam.model_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=723,
  serialized_end=764,
)


_CANDISABLEMODELRESPONSE = _descriptor.Descriptor(
  name='CanDisableModelResponse',
  full_name='orchestrator.CanDisableModelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='can_disable', full_name='orchestrator.CanDisableModelResponse.can_disable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=766,
  serialized_end=812,
)


_DISABLEMODELPARAM = _descriptor.Descriptor(
  name='DisableModelParam',
  full_name='orchestrator.DisableModelParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_key', full_name='orchestrator.DisableModelParam.model_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=814,
  serialized_end=852,
)


_GETMODELPARAM = _descriptor.Descriptor(
  name='GetModelParam',
  full_name='orchestrator.GetModelParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.GetModelParam.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=854,
  serialized_end=882,
)


_QUERYMODELSPARAM = _descriptor.Descriptor(
  name='QueryModelsParam',
  full_name='orchestrator.QueryModelsParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='orchestrator.QueryModelsParam.category', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='orchestrator.QueryModelsParam.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='orchestrator.QueryModelsParam.page_size', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=884,
  serialized_end=988,
)


_QUERYMODELSRESPONSE = _descriptor.Descriptor(
  name='QueryModelsResponse',
  full_name='orchestrator.QueryModelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='models', full_name='orchestrator.QueryModelsResponse.models', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='orchestrator.QueryModelsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=990,
  serialized_end=1073,
)


_DISABLEMODELRESPONSE = _descriptor.Descriptor(
  name='DisableModelResponse',
  full_name='orchestrator.DisableModelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1075,
  serialized_end=1097,
)

_MODEL.fields_by_name['category'].enum_type = _MODELCATEGORY
_MODEL.fields_by_name['address'].message_type = common__pb2._ADDRESSABLE
_MODEL.fields_by_name['permissions'].message_type = common__pb2._PERMISSIONS
_MODEL.fields_by_name['creation_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_NEWMODEL.fields_by_name['category'].enum_type = _MODELCATEGORY
_NEWMODEL.fields_by_name['address'].message_type = common__pb2._ADDRESSABLE
_REGISTERMODELSPARAM.fields_by_name['models'].message_type = _NEWMODEL
_REGISTERMODELSRESPONSE.fields_by_name['models'].message_type = _MODEL
_GETCOMPUTETASKMODELSRESPONSE.fields_by_name['models'].message_type = _MODEL
_QUERYMODELSPARAM.fields_by_name['category'].enum_type = _MODELCATEGORY
_QUERYMODELSRESPONSE.fields_by_name['models'].message_type = _MODEL
DESCRIPTOR.message_types_by_name['Model'] = _MODEL
DESCRIPTOR.message_types_by_name['NewModel'] = _NEWMODEL
DESCRIPTOR.message_types_by_name['RegisterModelsParam'] = _REGISTERMODELSPARAM
DESCRIPTOR.message_types_by_name['RegisterModelsResponse'] = _REGISTERMODELSRESPONSE
DESCRIPTOR.message_types_by_name['GetComputeTaskModelsParam'] = _GETCOMPUTETASKMODELSPARAM
DESCRIPTOR.message_types_by_name['GetComputeTaskModelsResponse'] = _GETCOMPUTETASKMODELSRESPONSE
DESCRIPTOR.message_types_by_name['CanDisableModelParam'] = _CANDISABLEMODELPARAM
DESCRIPTOR.message_types_by_name['CanDisableModelResponse'] = _CANDISABLEMODELRESPONSE
DESCRIPTOR.message_types_by_name['DisableModelParam'] = _DISABLEMODELPARAM
DESCRIPTOR.message_types_by_name['GetModelParam'] = _GETMODELPARAM
DESCRIPTOR.message_types_by_name['QueryModelsParam'] = _QUERYMODELSPARAM
DESCRIPTOR.message_types_by_name['QueryModelsResponse'] = _QUERYMODELSRESPONSE
DESCRIPTOR.message_types_by_name['DisableModelResponse'] = _DISABLEMODELRESPONSE
DESCRIPTOR.enum_types_by_name['ModelCategory'] = _MODELCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), {
  'DESCRIPTOR' : _MODEL,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.Model)
  })
_sym_db.RegisterMessage(Model)

NewModel = _reflection.GeneratedProtocolMessageType('NewModel', (_message.Message,), {
  'DESCRIPTOR' : _NEWMODEL,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewModel)
  })
_sym_db.RegisterMessage(NewModel)

RegisterModelsParam = _reflection.GeneratedProtocolMessageType('RegisterModelsParam', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERMODELSPARAM,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.RegisterModelsParam)
  })
_sym_db.RegisterMessage(RegisterModelsParam)

RegisterModelsResponse = _reflection.GeneratedProtocolMessageType('RegisterModelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERMODELSRESPONSE,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.RegisterModelsResponse)
  })
_sym_db.RegisterMessage(RegisterModelsResponse)

GetComputeTaskModelsParam = _reflection.GeneratedProtocolMessageType('GetComputeTaskModelsParam', (_message.Message,), {
  'DESCRIPTOR' : _GETCOMPUTETASKMODELSPARAM,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.GetComputeTaskModelsParam)
  })
_sym_db.RegisterMessage(GetComputeTaskModelsParam)

GetComputeTaskModelsResponse = _reflection.GeneratedProtocolMessageType('GetComputeTaskModelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCOMPUTETASKMODELSRESPONSE,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.GetComputeTaskModelsResponse)
  })
_sym_db.RegisterMessage(GetComputeTaskModelsResponse)

CanDisableModelParam = _reflection.GeneratedProtocolMessageType('CanDisableModelParam', (_message.Message,), {
  'DESCRIPTOR' : _CANDISABLEMODELPARAM,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.CanDisableModelParam)
  })
_sym_db.RegisterMessage(CanDisableModelParam)

CanDisableModelResponse = _reflection.GeneratedProtocolMessageType('CanDisableModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANDISABLEMODELRESPONSE,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.CanDisableModelResponse)
  })
_sym_db.RegisterMessage(CanDisableModelResponse)

DisableModelParam = _reflection.GeneratedProtocolMessageType('DisableModelParam', (_message.Message,), {
  'DESCRIPTOR' : _DISABLEMODELPARAM,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.DisableModelParam)
  })
_sym_db.RegisterMessage(DisableModelParam)

GetModelParam = _reflection.GeneratedProtocolMessageType('GetModelParam', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELPARAM,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.GetModelParam)
  })
_sym_db.RegisterMessage(GetModelParam)

QueryModelsParam = _reflection.GeneratedProtocolMessageType('QueryModelsParam', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMODELSPARAM,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryModelsParam)
  })
_sym_db.RegisterMessage(QueryModelsParam)

QueryModelsResponse = _reflection.GeneratedProtocolMessageType('QueryModelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMODELSRESPONSE,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryModelsResponse)
  })
_sym_db.RegisterMessage(QueryModelsResponse)

DisableModelResponse = _reflection.GeneratedProtocolMessageType('DisableModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _DISABLEMODELRESPONSE,
  '__module__' : 'model_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.DisableModelResponse)
  })
_sym_db.RegisterMessage(DisableModelResponse)


DESCRIPTOR._options = None

_MODELSERVICE = _descriptor.ServiceDescriptor(
  name='ModelService',
  full_name='orchestrator.ModelService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1170,
  serialized_end=1894,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterModel',
    full_name='orchestrator.ModelService.RegisterModel',
    index=0,
    containing_service=None,
    input_type=_NEWMODEL,
    output_type=_MODEL,
    serialized_options=b'\210\002\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterModels',
    full_name='orchestrator.ModelService.RegisterModels',
    index=1,
    containing_service=None,
    input_type=_REGISTERMODELSPARAM,
    output_type=_REGISTERMODELSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetModel',
    full_name='orchestrator.ModelService.GetModel',
    index=2,
    containing_service=None,
    input_type=_GETMODELPARAM,
    output_type=_MODEL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryModels',
    full_name='orchestrator.ModelService.QueryModels',
    index=3,
    containing_service=None,
    input_type=_QUERYMODELSPARAM,
    output_type=_QUERYMODELSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetComputeTaskOutputModels',
    full_name='orchestrator.ModelService.GetComputeTaskOutputModels',
    index=4,
    containing_service=None,
    input_type=_GETCOMPUTETASKMODELSPARAM,
    output_type=_GETCOMPUTETASKMODELSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetComputeTaskInputModels',
    full_name='orchestrator.ModelService.GetComputeTaskInputModels',
    index=5,
    containing_service=None,
    input_type=_GETCOMPUTETASKMODELSPARAM,
    output_type=_GETCOMPUTETASKMODELSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CanDisableModel',
    full_name='orchestrator.ModelService.CanDisableModel',
    index=6,
    containing_service=None,
    input_type=_CANDISABLEMODELPARAM,
    output_type=_CANDISABLEMODELRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DisableModel',
    full_name='orchestrator.ModelService.DisableModel',
    index=7,
    containing_service=None,
    input_type=_DISABLEMODELPARAM,
    output_type=_DISABLEMODELRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MODELSERVICE)

DESCRIPTOR.services_by_name['ModelService'] = _MODELSERVICE

# @@protoc_insertion_point(module_scope)
