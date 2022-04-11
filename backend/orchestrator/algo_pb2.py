# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: algo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nalgo.proto\x12\x0corchestrator\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0c\x63ommon.proto\"\x84\x03\n\x04\x41lgo\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12,\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32\x1a.orchestrator.AlgoCategory\x12.\n\x0b\x64\x65scription\x18\x04 \x01(\x0b\x32\x19.orchestrator.Addressable\x12,\n\talgorithm\x18\x05 \x01(\x0b\x32\x19.orchestrator.Addressable\x12.\n\x0bpermissions\x18\x06 \x01(\x0b\x32\x19.orchestrator.Permissions\x12\r\n\x05owner\x18\x07 \x01(\t\x12\x31\n\rcreation_date\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x08metadata\x18\x10 \x03(\x0b\x32 .orchestrator.Algo.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xcf\x02\n\x07NewAlgo\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12,\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32\x1a.orchestrator.AlgoCategory\x12.\n\x0b\x64\x65scription\x18\x04 \x01(\x0b\x32\x19.orchestrator.Addressable\x12,\n\talgorithm\x18\x05 \x01(\x0b\x32\x19.orchestrator.Addressable\x12\x35\n\x0fnew_permissions\x18\x06 \x01(\x0b\x32\x1c.orchestrator.NewPermissions\x12\x35\n\x08metadata\x18\x11 \x03(\x0b\x32#.orchestrator.NewAlgo.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1b\n\x0cGetAlgoParam\x12\x0b\n\x03key\x18\x01 \x01(\t\"P\n\x12QueryAlgosResponse\x12!\n\x05\x41lgos\x18\x01 \x03(\x0b\x32\x12.orchestrator.Algo\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"[\n\x0f\x41lgoQueryFilter\x12.\n\ncategories\x18\x01 \x03(\x0e\x32\x1a.orchestrator.AlgoCategory\x12\x18\n\x10\x63ompute_plan_key\x18\x02 \x01(\t\"g\n\x0fQueryAlgosParam\x12\x12\n\npage_token\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\r\x12-\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x1d.orchestrator.AlgoQueryFilter*j\n\x0c\x41lgoCategory\x12\x10\n\x0c\x41LGO_UNKNOWN\x10\x00\x12\x0f\n\x0b\x41LGO_SIMPLE\x10\x01\x12\x12\n\x0e\x41LGO_AGGREGATE\x10\x02\x12\x12\n\x0e\x41LGO_COMPOSITE\x10\x03\x12\x0f\n\x0b\x41LGO_METRIC\x10\x04\x32\xd2\x01\n\x0b\x41lgoService\x12\x39\n\x0cRegisterAlgo\x12\x15.orchestrator.NewAlgo\x1a\x12.orchestrator.Algo\x12\x39\n\x07GetAlgo\x12\x1a.orchestrator.GetAlgoParam\x1a\x12.orchestrator.Algo\x12M\n\nQueryAlgos\x12\x1d.orchestrator.QueryAlgosParam\x1a .orchestrator.QueryAlgosResponseB)Z\'github.com/owkin/orchestrator/lib/assetb\x06proto3')

_ALGOCATEGORY = DESCRIPTOR.enum_types_by_name['AlgoCategory']
AlgoCategory = enum_type_wrapper.EnumTypeWrapper(_ALGOCATEGORY)
ALGO_UNKNOWN = 0
ALGO_SIMPLE = 1
ALGO_AGGREGATE = 2
ALGO_COMPOSITE = 3
ALGO_METRIC = 4


_ALGO = DESCRIPTOR.message_types_by_name['Algo']
_ALGO_METADATAENTRY = _ALGO.nested_types_by_name['MetadataEntry']
_NEWALGO = DESCRIPTOR.message_types_by_name['NewAlgo']
_NEWALGO_METADATAENTRY = _NEWALGO.nested_types_by_name['MetadataEntry']
_GETALGOPARAM = DESCRIPTOR.message_types_by_name['GetAlgoParam']
_QUERYALGOSRESPONSE = DESCRIPTOR.message_types_by_name['QueryAlgosResponse']
_ALGOQUERYFILTER = DESCRIPTOR.message_types_by_name['AlgoQueryFilter']
_QUERYALGOSPARAM = DESCRIPTOR.message_types_by_name['QueryAlgosParam']
Algo = _reflection.GeneratedProtocolMessageType('Algo', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALGO_METADATAENTRY,
    '__module__' : 'algo_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.Algo.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _ALGO,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.Algo)
  })
_sym_db.RegisterMessage(Algo)
_sym_db.RegisterMessage(Algo.MetadataEntry)

NewAlgo = _reflection.GeneratedProtocolMessageType('NewAlgo', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _NEWALGO_METADATAENTRY,
    '__module__' : 'algo_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.NewAlgo.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _NEWALGO,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewAlgo)
  })
_sym_db.RegisterMessage(NewAlgo)
_sym_db.RegisterMessage(NewAlgo.MetadataEntry)

GetAlgoParam = _reflection.GeneratedProtocolMessageType('GetAlgoParam', (_message.Message,), {
  'DESCRIPTOR' : _GETALGOPARAM,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.GetAlgoParam)
  })
_sym_db.RegisterMessage(GetAlgoParam)

QueryAlgosResponse = _reflection.GeneratedProtocolMessageType('QueryAlgosResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALGOSRESPONSE,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryAlgosResponse)
  })
_sym_db.RegisterMessage(QueryAlgosResponse)

AlgoQueryFilter = _reflection.GeneratedProtocolMessageType('AlgoQueryFilter', (_message.Message,), {
  'DESCRIPTOR' : _ALGOQUERYFILTER,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.AlgoQueryFilter)
  })
_sym_db.RegisterMessage(AlgoQueryFilter)

QueryAlgosParam = _reflection.GeneratedProtocolMessageType('QueryAlgosParam', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALGOSPARAM,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryAlgosParam)
  })
_sym_db.RegisterMessage(QueryAlgosParam)

_ALGOSERVICE = DESCRIPTOR.services_by_name['AlgoService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\'github.com/owkin/orchestrator/lib/asset'
  _ALGO_METADATAENTRY._options = None
  _ALGO_METADATAENTRY._serialized_options = b'8\001'
  _NEWALGO_METADATAENTRY._options = None
  _NEWALGO_METADATAENTRY._serialized_options = b'8\001'
  _ALGOCATEGORY._serialized_start=1113
  _ALGOCATEGORY._serialized_end=1219
  _ALGO._serialized_start=76
  _ALGO._serialized_end=464
  _ALGO_METADATAENTRY._serialized_start=417
  _ALGO_METADATAENTRY._serialized_end=464
  _NEWALGO._serialized_start=467
  _NEWALGO._serialized_end=802
  _NEWALGO_METADATAENTRY._serialized_start=417
  _NEWALGO_METADATAENTRY._serialized_end=464
  _GETALGOPARAM._serialized_start=804
  _GETALGOPARAM._serialized_end=831
  _QUERYALGOSRESPONSE._serialized_start=833
  _QUERYALGOSRESPONSE._serialized_end=913
  _ALGOQUERYFILTER._serialized_start=915
  _ALGOQUERYFILTER._serialized_end=1006
  _QUERYALGOSPARAM._serialized_start=1008
  _QUERYALGOSPARAM._serialized_end=1111
  _ALGOSERVICE._serialized_start=1222
  _ALGOSERVICE._serialized_end=1432
# @@protoc_insertion_point(module_scope)
