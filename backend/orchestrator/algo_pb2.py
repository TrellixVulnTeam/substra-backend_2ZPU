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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nalgo.proto\x12\x0corchestrator\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0c\x63ommon.proto\"V\n\tAlgoInput\x12%\n\x04kind\x18\x01 \x01(\x0e\x32\x17.orchestrator.AssetKind\x12\x10\n\x08multiple\x18\x02 \x01(\x08\x12\x10\n\x08optional\x18\x03 \x01(\x08\"E\n\nAlgoOutput\x12%\n\x04kind\x18\x01 \x01(\x0e\x32\x17.orchestrator.AssetKind\x12\x10\n\x08multiple\x18\x02 \x01(\x08\"\xf8\x04\n\x04\x41lgo\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12,\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32\x1a.orchestrator.AlgoCategory\x12.\n\x0b\x64\x65scription\x18\x04 \x01(\x0b\x32\x19.orchestrator.Addressable\x12,\n\talgorithm\x18\x05 \x01(\x0b\x32\x19.orchestrator.Addressable\x12.\n\x0bpermissions\x18\x06 \x01(\x0b\x32\x19.orchestrator.Permissions\x12\r\n\x05owner\x18\x07 \x01(\t\x12\x31\n\rcreation_date\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x08metadata\x18\x10 \x03(\x0b\x32 .orchestrator.Algo.MetadataEntry\x12.\n\x06inputs\x18\x11 \x03(\x0b\x32\x1e.orchestrator.Algo.InputsEntry\x12\x30\n\x07outputs\x18\x12 \x03(\x0b\x32\x1f.orchestrator.Algo.OutputsEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x46\n\x0bInputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.orchestrator.AlgoInput:\x02\x38\x01\x1aH\n\x0cOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.orchestrator.AlgoOutput:\x02\x38\x01\"\xc9\x04\n\x07NewAlgo\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12,\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32\x1a.orchestrator.AlgoCategory\x12.\n\x0b\x64\x65scription\x18\x04 \x01(\x0b\x32\x19.orchestrator.Addressable\x12,\n\talgorithm\x18\x05 \x01(\x0b\x32\x19.orchestrator.Addressable\x12\x35\n\x0fnew_permissions\x18\x06 \x01(\x0b\x32\x1c.orchestrator.NewPermissions\x12\x35\n\x08metadata\x18\x11 \x03(\x0b\x32#.orchestrator.NewAlgo.MetadataEntry\x12\x31\n\x06inputs\x18\x12 \x03(\x0b\x32!.orchestrator.NewAlgo.InputsEntry\x12\x33\n\x07outputs\x18\x13 \x03(\x0b\x32\".orchestrator.NewAlgo.OutputsEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x46\n\x0bInputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.orchestrator.AlgoInput:\x02\x38\x01\x1aH\n\x0cOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.orchestrator.AlgoOutput:\x02\x38\x01\"\x1b\n\x0cGetAlgoParam\x12\x0b\n\x03key\x18\x01 \x01(\t\"P\n\x12QueryAlgosResponse\x12!\n\x05\x41lgos\x18\x01 \x03(\x0b\x32\x12.orchestrator.Algo\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"[\n\x0f\x41lgoQueryFilter\x12.\n\ncategories\x18\x01 \x03(\x0e\x32\x1a.orchestrator.AlgoCategory\x12\x18\n\x10\x63ompute_plan_key\x18\x02 \x01(\t\"g\n\x0fQueryAlgosParam\x12\x12\n\npage_token\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\r\x12-\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x1d.orchestrator.AlgoQueryFilter*j\n\x0c\x41lgoCategory\x12\x10\n\x0c\x41LGO_UNKNOWN\x10\x00\x12\x0f\n\x0b\x41LGO_SIMPLE\x10\x01\x12\x12\n\x0e\x41LGO_AGGREGATE\x10\x02\x12\x12\n\x0e\x41LGO_COMPOSITE\x10\x03\x12\x0f\n\x0b\x41LGO_METRIC\x10\x04\x32\xd2\x01\n\x0b\x41lgoService\x12\x39\n\x0cRegisterAlgo\x12\x15.orchestrator.NewAlgo\x1a\x12.orchestrator.Algo\x12\x39\n\x07GetAlgo\x12\x1a.orchestrator.GetAlgoParam\x1a\x12.orchestrator.Algo\x12M\n\nQueryAlgos\x12\x1d.orchestrator.QueryAlgosParam\x1a .orchestrator.QueryAlgosResponseB)Z\'github.com/owkin/orchestrator/lib/assetb\x06proto3')

_ALGOCATEGORY = DESCRIPTOR.enum_types_by_name['AlgoCategory']
AlgoCategory = enum_type_wrapper.EnumTypeWrapper(_ALGOCATEGORY)
ALGO_UNKNOWN = 0
ALGO_SIMPLE = 1
ALGO_AGGREGATE = 2
ALGO_COMPOSITE = 3
ALGO_METRIC = 4


_ALGOINPUT = DESCRIPTOR.message_types_by_name['AlgoInput']
_ALGOOUTPUT = DESCRIPTOR.message_types_by_name['AlgoOutput']
_ALGO = DESCRIPTOR.message_types_by_name['Algo']
_ALGO_METADATAENTRY = _ALGO.nested_types_by_name['MetadataEntry']
_ALGO_INPUTSENTRY = _ALGO.nested_types_by_name['InputsEntry']
_ALGO_OUTPUTSENTRY = _ALGO.nested_types_by_name['OutputsEntry']
_NEWALGO = DESCRIPTOR.message_types_by_name['NewAlgo']
_NEWALGO_METADATAENTRY = _NEWALGO.nested_types_by_name['MetadataEntry']
_NEWALGO_INPUTSENTRY = _NEWALGO.nested_types_by_name['InputsEntry']
_NEWALGO_OUTPUTSENTRY = _NEWALGO.nested_types_by_name['OutputsEntry']
_GETALGOPARAM = DESCRIPTOR.message_types_by_name['GetAlgoParam']
_QUERYALGOSRESPONSE = DESCRIPTOR.message_types_by_name['QueryAlgosResponse']
_ALGOQUERYFILTER = DESCRIPTOR.message_types_by_name['AlgoQueryFilter']
_QUERYALGOSPARAM = DESCRIPTOR.message_types_by_name['QueryAlgosParam']
AlgoInput = _reflection.GeneratedProtocolMessageType('AlgoInput', (_message.Message,), {
  'DESCRIPTOR' : _ALGOINPUT,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.AlgoInput)
  })
_sym_db.RegisterMessage(AlgoInput)

AlgoOutput = _reflection.GeneratedProtocolMessageType('AlgoOutput', (_message.Message,), {
  'DESCRIPTOR' : _ALGOOUTPUT,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.AlgoOutput)
  })
_sym_db.RegisterMessage(AlgoOutput)

Algo = _reflection.GeneratedProtocolMessageType('Algo', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALGO_METADATAENTRY,
    '__module__' : 'algo_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.Algo.MetadataEntry)
    })
  ,

  'InputsEntry' : _reflection.GeneratedProtocolMessageType('InputsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALGO_INPUTSENTRY,
    '__module__' : 'algo_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.Algo.InputsEntry)
    })
  ,

  'OutputsEntry' : _reflection.GeneratedProtocolMessageType('OutputsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALGO_OUTPUTSENTRY,
    '__module__' : 'algo_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.Algo.OutputsEntry)
    })
  ,
  'DESCRIPTOR' : _ALGO,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.Algo)
  })
_sym_db.RegisterMessage(Algo)
_sym_db.RegisterMessage(Algo.MetadataEntry)
_sym_db.RegisterMessage(Algo.InputsEntry)
_sym_db.RegisterMessage(Algo.OutputsEntry)

NewAlgo = _reflection.GeneratedProtocolMessageType('NewAlgo', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _NEWALGO_METADATAENTRY,
    '__module__' : 'algo_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.NewAlgo.MetadataEntry)
    })
  ,

  'InputsEntry' : _reflection.GeneratedProtocolMessageType('InputsEntry', (_message.Message,), {
    'DESCRIPTOR' : _NEWALGO_INPUTSENTRY,
    '__module__' : 'algo_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.NewAlgo.InputsEntry)
    })
  ,

  'OutputsEntry' : _reflection.GeneratedProtocolMessageType('OutputsEntry', (_message.Message,), {
    'DESCRIPTOR' : _NEWALGO_OUTPUTSENTRY,
    '__module__' : 'algo_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.NewAlgo.OutputsEntry)
    })
  ,
  'DESCRIPTOR' : _NEWALGO,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewAlgo)
  })
_sym_db.RegisterMessage(NewAlgo)
_sym_db.RegisterMessage(NewAlgo.MetadataEntry)
_sym_db.RegisterMessage(NewAlgo.InputsEntry)
_sym_db.RegisterMessage(NewAlgo.OutputsEntry)

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
  _ALGO_INPUTSENTRY._options = None
  _ALGO_INPUTSENTRY._serialized_options = b'8\001'
  _ALGO_OUTPUTSENTRY._options = None
  _ALGO_OUTPUTSENTRY._serialized_options = b'8\001'
  _NEWALGO_METADATAENTRY._options = None
  _NEWALGO_METADATAENTRY._serialized_options = b'8\001'
  _NEWALGO_INPUTSENTRY._options = None
  _NEWALGO_INPUTSENTRY._serialized_options = b'8\001'
  _NEWALGO_OUTPUTSENTRY._options = None
  _NEWALGO_OUTPUTSENTRY._serialized_options = b'8\001'
  _ALGOCATEGORY._serialized_start=1766
  _ALGOCATEGORY._serialized_end=1872
  _ALGOINPUT._serialized_start=75
  _ALGOINPUT._serialized_end=161
  _ALGOOUTPUT._serialized_start=163
  _ALGOOUTPUT._serialized_end=232
  _ALGO._serialized_start=235
  _ALGO._serialized_end=867
  _ALGO_METADATAENTRY._serialized_start=674
  _ALGO_METADATAENTRY._serialized_end=721
  _ALGO_INPUTSENTRY._serialized_start=723
  _ALGO_INPUTSENTRY._serialized_end=793
  _ALGO_OUTPUTSENTRY._serialized_start=795
  _ALGO_OUTPUTSENTRY._serialized_end=867
  _NEWALGO._serialized_start=870
  _NEWALGO._serialized_end=1455
  _NEWALGO_METADATAENTRY._serialized_start=674
  _NEWALGO_METADATAENTRY._serialized_end=721
  _NEWALGO_INPUTSENTRY._serialized_start=723
  _NEWALGO_INPUTSENTRY._serialized_end=793
  _NEWALGO_OUTPUTSENTRY._serialized_start=795
  _NEWALGO_OUTPUTSENTRY._serialized_end=867
  _GETALGOPARAM._serialized_start=1457
  _GETALGOPARAM._serialized_end=1484
  _QUERYALGOSRESPONSE._serialized_start=1486
  _QUERYALGOSRESPONSE._serialized_end=1566
  _ALGOQUERYFILTER._serialized_start=1568
  _ALGOQUERYFILTER._serialized_end=1659
  _QUERYALGOSPARAM._serialized_start=1661
  _QUERYALGOSPARAM._serialized_end=1764
  _ALGOSERVICE._serialized_start=1875
  _ALGOSERVICE._serialized_end=2085
# @@protoc_insertion_point(module_scope)
