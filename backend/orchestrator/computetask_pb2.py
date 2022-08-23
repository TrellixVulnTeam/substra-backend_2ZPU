# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: computetask.proto
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
from . import algo_pb2 as algo__pb2
from . import model_pb2 as model__pb2
from . import datamanager_pb2 as datamanager__pb2
from . import datasample_pb2 as datasample__pb2
from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63omputetask.proto\x12\x0corchestrator\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\nalgo.proto\x1a\x0bmodel.proto\x1a\x11\x64\x61tamanager.proto\x1a\x10\x64\x61tasample.proto\x1a\x0c\x63ommon.proto\"I\n\x13ParentTaskOutputRef\x12\x17\n\x0fparent_task_key\x18\x01 \x01(\t\x12\x19\n\x11output_identifier\x18\x02 \x01(\t\"\x83\x01\n\x10\x43omputeTaskInput\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12\x13\n\tasset_key\x18\x02 \x01(\tH\x00\x12?\n\x12parent_task_output\x18\x03 \x01(\x0b\x32!.orchestrator.ParentTaskOutputRefH\x00\x42\x05\n\x03ref\"V\n\x11\x43omputeTaskOutput\x12.\n\x0bpermissions\x18\x01 \x01(\x0b\x32\x19.orchestrator.Permissions\x12\x11\n\ttransient\x18\x02 \x01(\x08\"\\\n\x14NewComputeTaskOutput\x12\x31\n\x0bpermissions\x18\x01 \x01(\x0b\x32\x1c.orchestrator.NewPermissions\x12\x11\n\ttransient\x18\x02 \x01(\x08\"\x99\x07\n\x0b\x43omputeTask\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32!.orchestrator.ComputeTaskCategory\x12 \n\x04\x61lgo\x18\x03 \x01(\x0b\x32\x12.orchestrator.Algo\x12\r\n\x05owner\x18\x04 \x01(\t\x12\x18\n\x10\x63ompute_plan_key\x18\x05 \x01(\t\x12\x18\n\x10parent_task_keys\x18\x06 \x03(\t\x12\x0c\n\x04rank\x18\x07 \x01(\x05\x12/\n\x06status\x18\x08 \x01(\x0e\x32\x1f.orchestrator.ComputeTaskStatus\x12\x0e\n\x06worker\x18\t \x01(\t\x12\x31\n\rcreation_date\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\x0flogs_permission\x18\x0b \x01(\x0b\x32\x18.orchestrator.Permission\x12*\n\x04test\x18\x0c \x01(\x0b\x32\x1a.orchestrator.TestTaskDataH\x00\x12,\n\x05train\x18\r \x01(\x0b\x32\x1b.orchestrator.TrainTaskDataH\x00\x12\x39\n\tcomposite\x18\x0e \x01(\x0b\x32$.orchestrator.CompositeTrainTaskDataH\x00\x12\x39\n\taggregate\x18\x0f \x01(\x0b\x32$.orchestrator.AggregateTrainTaskDataH\x00\x12\x30\n\x07predict\x18\x12 \x01(\x0b\x32\x1d.orchestrator.PredictTaskDataH\x00\x12\x39\n\x08metadata\x18\x10 \x03(\x0b\x32\'.orchestrator.ComputeTask.MetadataEntry\x12.\n\x06inputs\x18\x11 \x03(\x0b\x32\x1e.orchestrator.ComputeTaskInput\x12\x37\n\x07outputs\x18\x13 \x03(\x0b\x32&.orchestrator.ComputeTask.OutputsEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aO\n\x0cOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.orchestrator.ComputeTaskOutput:\x02\x38\x01\x42\x06\n\x04\x64\x61ta\"\xe0\x05\n\x0eNewComputeTask\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32!.orchestrator.ComputeTaskCategory\x12\x10\n\x08\x61lgo_key\x18\x03 \x01(\t\x12\x18\n\x10\x63ompute_plan_key\x18\x04 \x01(\t\x12\x18\n\x10parent_task_keys\x18\x05 \x03(\t\x12-\n\x04test\x18\x0c \x01(\x0b\x32\x1d.orchestrator.NewTestTaskDataH\x00\x12/\n\x05train\x18\r \x01(\x0b\x32\x1e.orchestrator.NewTrainTaskDataH\x00\x12<\n\tcomposite\x18\x0e \x01(\x0b\x32\'.orchestrator.NewCompositeTrainTaskDataH\x00\x12<\n\taggregate\x18\x0f \x01(\x0b\x32\'.orchestrator.NewAggregateTrainTaskDataH\x00\x12\x33\n\x07predict\x18\x12 \x01(\x0b\x32 .orchestrator.NewPredictTaskDataH\x00\x12<\n\x08metadata\x18\x10 \x03(\x0b\x32*.orchestrator.NewComputeTask.MetadataEntry\x12.\n\x06inputs\x18\x11 \x03(\x0b\x32\x1e.orchestrator.ComputeTaskInput\x12:\n\x07outputs\x18\x13 \x03(\x0b\x32).orchestrator.NewComputeTask.OutputsEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aR\n\x0cOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\".orchestrator.NewComputeTaskOutput:\x02\x38\x01\x42\x06\n\x04\x64\x61ta\"\\\n\rTrainTaskData\x12\x18\n\x10\x64\x61ta_manager_key\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_sample_keys\x18\x02 \x03(\tJ\x04\x08\x04\x10\x05R\x11model_permissions\"F\n\x10NewTrainTaskData\x12\x18\n\x10\x64\x61ta_manager_key\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_sample_keys\x18\x02 \x03(\t\"c\n\x0fPredictTaskData\x12\x18\n\x10\x64\x61ta_manager_key\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_sample_keys\x18\x02 \x03(\tJ\x04\x08\x03\x10\x04R\x16prediction_permissions\"H\n\x12NewPredictTaskData\x12\x18\n\x10\x64\x61ta_manager_key\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_sample_keys\x18\x02 \x03(\t\"U\n\x0cTestTaskData\x12\x18\n\x10\x64\x61ta_manager_key\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_sample_keys\x18\x02 \x03(\tJ\x04\x08\x03\x10\x04R\x0bmetric_keys\"X\n\x0fNewTestTaskData\x12\x18\n\x10\x64\x61ta_manager_key\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_sample_keys\x18\x02 \x03(\tJ\x04\x08\x03\x10\x04R\x0bmetric_keys\"}\n\x16\x43ompositeTrainTaskData\x12\x18\n\x10\x64\x61ta_manager_key\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_sample_keys\x18\x02 \x03(\tJ\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07R\x10head_permissionsR\x11trunk_permissions\"h\n\x19NewCompositeTrainTaskData\x12\x18\n\x10\x64\x61ta_manager_key\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_sample_keys\x18\x02 \x03(\tJ\x04\x08\x04\x10\x05R\x11trunk_permissions\"1\n\x16\x41ggregateTrainTaskDataJ\x04\x08\x02\x10\x03R\x11model_permissions\"+\n\x19NewAggregateTrainTaskData\x12\x0e\n\x06worker\x18\x02 \x01(\t\"A\n\x12RegisterTasksParam\x12+\n\x05tasks\x18\x01 \x03(\x0b\x32\x1c.orchestrator.NewComputeTask\"A\n\x15RegisterTasksResponse\x12(\n\x05tasks\x18\x01 \x03(\x0b\x32\x19.orchestrator.ComputeTask\"\xb3\x01\n\x0fTaskQueryFilter\x12\x0e\n\x06worker\x18\x01 \x01(\t\x12/\n\x06status\x18\x02 \x01(\x0e\x32\x1f.orchestrator.ComputeTaskStatus\x12\x33\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32!.orchestrator.ComputeTaskCategory\x12\x18\n\x10\x63ompute_plan_key\x18\x04 \x01(\t\x12\x10\n\x08\x61lgo_key\x18\x05 \x01(\t\"g\n\x0fQueryTasksParam\x12\x12\n\npage_token\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\r\x12-\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x1d.orchestrator.TaskQueryFilter\"W\n\x12QueryTasksResponse\x12(\n\x05tasks\x18\x01 \x03(\x0b\x32\x19.orchestrator.ComputeTask\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x1b\n\x0cGetTaskParam\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x9a\x01\n\x16\x43omputeTaskOutputAsset\x12\x18\n\x10\x63ompute_task_key\x18\x01 \x01(\t\x12&\n\x1e\x63ompute_task_output_identifier\x18\x02 \x01(\t\x12+\n\nasset_kind\x18\x03 \x01(\x0e\x32\x17.orchestrator.AssetKind\x12\x11\n\tasset_key\x18\x04 \x01(\t\"n\n\x14\x41pplyTaskActionParam\x12\x18\n\x10\x63ompute_task_key\x18\x01 \x01(\t\x12/\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x1f.orchestrator.ComputeTaskAction\x12\x0b\n\x03log\x18\x03 \x01(\t\"\x19\n\x17\x41pplyTaskActionResponse\"\xbe\x01\n\x15\x43omputeTaskInputAsset\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12$\n\x05model\x18\x02 \x01(\x0b\x32\x13.orchestrator.ModelH\x00\x12\x31\n\x0c\x64\x61ta_manager\x18\x03 \x01(\x0b\x32\x19.orchestrator.DataManagerH\x00\x12/\n\x0b\x64\x61ta_sample\x18\x04 \x01(\x0b\x32\x18.orchestrator.DataSampleH\x00\x42\x07\n\x05\x61sset\"3\n\x17GetTaskInputAssetsParam\x12\x18\n\x10\x63ompute_task_key\x18\x01 \x01(\t\"Q\n\x1aGetTaskInputAssetsResponse\x12\x33\n\x06\x61ssets\x18\x01 \x03(\x0b\x32#.orchestrator.ComputeTaskInputAsset\"B\n\x12\x44isableOutputParam\x12\x18\n\x10\x63ompute_task_key\x18\x01 \x01(\t\x12\x12\n\nidentifier\x18\x02 \x01(\t\"\x17\n\x15\x44isableOutputResponse*\x80\x01\n\x13\x43omputeTaskCategory\x12\x10\n\x0cTASK_UNKNOWN\x10\x00\x12\x0e\n\nTASK_TRAIN\x10\x01\x12\x12\n\x0eTASK_AGGREGATE\x10\x02\x12\x12\n\x0eTASK_COMPOSITE\x10\x03\x12\r\n\tTASK_TEST\x10\x04\x12\x10\n\x0cTASK_PREDICT\x10\x05*\x97\x01\n\x11\x43omputeTaskStatus\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x12\n\x0eSTATUS_WAITING\x10\x01\x12\x0f\n\x0bSTATUS_TODO\x10\x02\x12\x10\n\x0cSTATUS_DOING\x10\x03\x12\x0f\n\x0bSTATUS_DONE\x10\x04\x12\x13\n\x0fSTATUS_CANCELED\x10\x05\x12\x11\n\rSTATUS_FAILED\x10\x06*\x8b\x01\n\x11\x43omputeTaskAction\x12\x17\n\x13TASK_ACTION_UNKNOWN\x10\x00\x12\x15\n\x11TASK_ACTION_DOING\x10\x01\x12\x18\n\x14TASK_ACTION_CANCELED\x10\x02\x12\x16\n\x12TASK_ACTION_FAILED\x10\x03\x12\x14\n\x10TASK_ACTION_DONE\x10\x04\x32\x9a\x04\n\x12\x43omputeTaskService\x12V\n\rRegisterTasks\x12 .orchestrator.RegisterTasksParam\x1a#.orchestrator.RegisterTasksResponse\x12M\n\nQueryTasks\x12\x1d.orchestrator.QueryTasksParam\x1a .orchestrator.QueryTasksResponse\x12@\n\x07GetTask\x12\x1a.orchestrator.GetTaskParam\x1a\x19.orchestrator.ComputeTask\x12\\\n\x0f\x41pplyTaskAction\x12\".orchestrator.ApplyTaskActionParam\x1a%.orchestrator.ApplyTaskActionResponse\x12\x65\n\x12GetTaskInputAssets\x12%.orchestrator.GetTaskInputAssetsParam\x1a(.orchestrator.GetTaskInputAssetsResponse\x12V\n\rDisableOutput\x12 .orchestrator.DisableOutputParam\x1a#.orchestrator.DisableOutputResponseB+Z)github.com/substra/orchestrator/lib/assetb\x06proto3')

_COMPUTETASKCATEGORY = DESCRIPTOR.enum_types_by_name['ComputeTaskCategory']
ComputeTaskCategory = enum_type_wrapper.EnumTypeWrapper(_COMPUTETASKCATEGORY)
_COMPUTETASKSTATUS = DESCRIPTOR.enum_types_by_name['ComputeTaskStatus']
ComputeTaskStatus = enum_type_wrapper.EnumTypeWrapper(_COMPUTETASKSTATUS)
_COMPUTETASKACTION = DESCRIPTOR.enum_types_by_name['ComputeTaskAction']
ComputeTaskAction = enum_type_wrapper.EnumTypeWrapper(_COMPUTETASKACTION)
TASK_UNKNOWN = 0
TASK_TRAIN = 1
TASK_AGGREGATE = 2
TASK_COMPOSITE = 3
TASK_TEST = 4
TASK_PREDICT = 5
STATUS_UNKNOWN = 0
STATUS_WAITING = 1
STATUS_TODO = 2
STATUS_DOING = 3
STATUS_DONE = 4
STATUS_CANCELED = 5
STATUS_FAILED = 6
TASK_ACTION_UNKNOWN = 0
TASK_ACTION_DOING = 1
TASK_ACTION_CANCELED = 2
TASK_ACTION_FAILED = 3
TASK_ACTION_DONE = 4


_PARENTTASKOUTPUTREF = DESCRIPTOR.message_types_by_name['ParentTaskOutputRef']
_COMPUTETASKINPUT = DESCRIPTOR.message_types_by_name['ComputeTaskInput']
_COMPUTETASKOUTPUT = DESCRIPTOR.message_types_by_name['ComputeTaskOutput']
_NEWCOMPUTETASKOUTPUT = DESCRIPTOR.message_types_by_name['NewComputeTaskOutput']
_COMPUTETASK = DESCRIPTOR.message_types_by_name['ComputeTask']
_COMPUTETASK_METADATAENTRY = _COMPUTETASK.nested_types_by_name['MetadataEntry']
_COMPUTETASK_OUTPUTSENTRY = _COMPUTETASK.nested_types_by_name['OutputsEntry']
_NEWCOMPUTETASK = DESCRIPTOR.message_types_by_name['NewComputeTask']
_NEWCOMPUTETASK_METADATAENTRY = _NEWCOMPUTETASK.nested_types_by_name['MetadataEntry']
_NEWCOMPUTETASK_OUTPUTSENTRY = _NEWCOMPUTETASK.nested_types_by_name['OutputsEntry']
_TRAINTASKDATA = DESCRIPTOR.message_types_by_name['TrainTaskData']
_NEWTRAINTASKDATA = DESCRIPTOR.message_types_by_name['NewTrainTaskData']
_PREDICTTASKDATA = DESCRIPTOR.message_types_by_name['PredictTaskData']
_NEWPREDICTTASKDATA = DESCRIPTOR.message_types_by_name['NewPredictTaskData']
_TESTTASKDATA = DESCRIPTOR.message_types_by_name['TestTaskData']
_NEWTESTTASKDATA = DESCRIPTOR.message_types_by_name['NewTestTaskData']
_COMPOSITETRAINTASKDATA = DESCRIPTOR.message_types_by_name['CompositeTrainTaskData']
_NEWCOMPOSITETRAINTASKDATA = DESCRIPTOR.message_types_by_name['NewCompositeTrainTaskData']
_AGGREGATETRAINTASKDATA = DESCRIPTOR.message_types_by_name['AggregateTrainTaskData']
_NEWAGGREGATETRAINTASKDATA = DESCRIPTOR.message_types_by_name['NewAggregateTrainTaskData']
_REGISTERTASKSPARAM = DESCRIPTOR.message_types_by_name['RegisterTasksParam']
_REGISTERTASKSRESPONSE = DESCRIPTOR.message_types_by_name['RegisterTasksResponse']
_TASKQUERYFILTER = DESCRIPTOR.message_types_by_name['TaskQueryFilter']
_QUERYTASKSPARAM = DESCRIPTOR.message_types_by_name['QueryTasksParam']
_QUERYTASKSRESPONSE = DESCRIPTOR.message_types_by_name['QueryTasksResponse']
_GETTASKPARAM = DESCRIPTOR.message_types_by_name['GetTaskParam']
_COMPUTETASKOUTPUTASSET = DESCRIPTOR.message_types_by_name['ComputeTaskOutputAsset']
_APPLYTASKACTIONPARAM = DESCRIPTOR.message_types_by_name['ApplyTaskActionParam']
_APPLYTASKACTIONRESPONSE = DESCRIPTOR.message_types_by_name['ApplyTaskActionResponse']
_COMPUTETASKINPUTASSET = DESCRIPTOR.message_types_by_name['ComputeTaskInputAsset']
_GETTASKINPUTASSETSPARAM = DESCRIPTOR.message_types_by_name['GetTaskInputAssetsParam']
_GETTASKINPUTASSETSRESPONSE = DESCRIPTOR.message_types_by_name['GetTaskInputAssetsResponse']
_DISABLEOUTPUTPARAM = DESCRIPTOR.message_types_by_name['DisableOutputParam']
_DISABLEOUTPUTRESPONSE = DESCRIPTOR.message_types_by_name['DisableOutputResponse']
ParentTaskOutputRef = _reflection.GeneratedProtocolMessageType('ParentTaskOutputRef', (_message.Message,), {
  'DESCRIPTOR' : _PARENTTASKOUTPUTREF,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.ParentTaskOutputRef)
  })
_sym_db.RegisterMessage(ParentTaskOutputRef)

ComputeTaskInput = _reflection.GeneratedProtocolMessageType('ComputeTaskInput', (_message.Message,), {
  'DESCRIPTOR' : _COMPUTETASKINPUT,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.ComputeTaskInput)
  })
_sym_db.RegisterMessage(ComputeTaskInput)

ComputeTaskOutput = _reflection.GeneratedProtocolMessageType('ComputeTaskOutput', (_message.Message,), {
  'DESCRIPTOR' : _COMPUTETASKOUTPUT,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.ComputeTaskOutput)
  })
_sym_db.RegisterMessage(ComputeTaskOutput)

NewComputeTaskOutput = _reflection.GeneratedProtocolMessageType('NewComputeTaskOutput', (_message.Message,), {
  'DESCRIPTOR' : _NEWCOMPUTETASKOUTPUT,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewComputeTaskOutput)
  })
_sym_db.RegisterMessage(NewComputeTaskOutput)

ComputeTask = _reflection.GeneratedProtocolMessageType('ComputeTask', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _COMPUTETASK_METADATAENTRY,
    '__module__' : 'computetask_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.ComputeTask.MetadataEntry)
    })
  ,

  'OutputsEntry' : _reflection.GeneratedProtocolMessageType('OutputsEntry', (_message.Message,), {
    'DESCRIPTOR' : _COMPUTETASK_OUTPUTSENTRY,
    '__module__' : 'computetask_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.ComputeTask.OutputsEntry)
    })
  ,
  'DESCRIPTOR' : _COMPUTETASK,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.ComputeTask)
  })
_sym_db.RegisterMessage(ComputeTask)
_sym_db.RegisterMessage(ComputeTask.MetadataEntry)
_sym_db.RegisterMessage(ComputeTask.OutputsEntry)

NewComputeTask = _reflection.GeneratedProtocolMessageType('NewComputeTask', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _NEWCOMPUTETASK_METADATAENTRY,
    '__module__' : 'computetask_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.NewComputeTask.MetadataEntry)
    })
  ,

  'OutputsEntry' : _reflection.GeneratedProtocolMessageType('OutputsEntry', (_message.Message,), {
    'DESCRIPTOR' : _NEWCOMPUTETASK_OUTPUTSENTRY,
    '__module__' : 'computetask_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.NewComputeTask.OutputsEntry)
    })
  ,
  'DESCRIPTOR' : _NEWCOMPUTETASK,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewComputeTask)
  })
_sym_db.RegisterMessage(NewComputeTask)
_sym_db.RegisterMessage(NewComputeTask.MetadataEntry)
_sym_db.RegisterMessage(NewComputeTask.OutputsEntry)

TrainTaskData = _reflection.GeneratedProtocolMessageType('TrainTaskData', (_message.Message,), {
  'DESCRIPTOR' : _TRAINTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.TrainTaskData)
  })
_sym_db.RegisterMessage(TrainTaskData)

NewTrainTaskData = _reflection.GeneratedProtocolMessageType('NewTrainTaskData', (_message.Message,), {
  'DESCRIPTOR' : _NEWTRAINTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewTrainTaskData)
  })
_sym_db.RegisterMessage(NewTrainTaskData)

PredictTaskData = _reflection.GeneratedProtocolMessageType('PredictTaskData', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.PredictTaskData)
  })
_sym_db.RegisterMessage(PredictTaskData)

NewPredictTaskData = _reflection.GeneratedProtocolMessageType('NewPredictTaskData', (_message.Message,), {
  'DESCRIPTOR' : _NEWPREDICTTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewPredictTaskData)
  })
_sym_db.RegisterMessage(NewPredictTaskData)

TestTaskData = _reflection.GeneratedProtocolMessageType('TestTaskData', (_message.Message,), {
  'DESCRIPTOR' : _TESTTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.TestTaskData)
  })
_sym_db.RegisterMessage(TestTaskData)

NewTestTaskData = _reflection.GeneratedProtocolMessageType('NewTestTaskData', (_message.Message,), {
  'DESCRIPTOR' : _NEWTESTTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewTestTaskData)
  })
_sym_db.RegisterMessage(NewTestTaskData)

CompositeTrainTaskData = _reflection.GeneratedProtocolMessageType('CompositeTrainTaskData', (_message.Message,), {
  'DESCRIPTOR' : _COMPOSITETRAINTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.CompositeTrainTaskData)
  })
_sym_db.RegisterMessage(CompositeTrainTaskData)

NewCompositeTrainTaskData = _reflection.GeneratedProtocolMessageType('NewCompositeTrainTaskData', (_message.Message,), {
  'DESCRIPTOR' : _NEWCOMPOSITETRAINTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewCompositeTrainTaskData)
  })
_sym_db.RegisterMessage(NewCompositeTrainTaskData)

AggregateTrainTaskData = _reflection.GeneratedProtocolMessageType('AggregateTrainTaskData', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATETRAINTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.AggregateTrainTaskData)
  })
_sym_db.RegisterMessage(AggregateTrainTaskData)

NewAggregateTrainTaskData = _reflection.GeneratedProtocolMessageType('NewAggregateTrainTaskData', (_message.Message,), {
  'DESCRIPTOR' : _NEWAGGREGATETRAINTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewAggregateTrainTaskData)
  })
_sym_db.RegisterMessage(NewAggregateTrainTaskData)

RegisterTasksParam = _reflection.GeneratedProtocolMessageType('RegisterTasksParam', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERTASKSPARAM,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.RegisterTasksParam)
  })
_sym_db.RegisterMessage(RegisterTasksParam)

RegisterTasksResponse = _reflection.GeneratedProtocolMessageType('RegisterTasksResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERTASKSRESPONSE,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.RegisterTasksResponse)
  })
_sym_db.RegisterMessage(RegisterTasksResponse)

TaskQueryFilter = _reflection.GeneratedProtocolMessageType('TaskQueryFilter', (_message.Message,), {
  'DESCRIPTOR' : _TASKQUERYFILTER,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.TaskQueryFilter)
  })
_sym_db.RegisterMessage(TaskQueryFilter)

QueryTasksParam = _reflection.GeneratedProtocolMessageType('QueryTasksParam', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTASKSPARAM,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryTasksParam)
  })
_sym_db.RegisterMessage(QueryTasksParam)

QueryTasksResponse = _reflection.GeneratedProtocolMessageType('QueryTasksResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTASKSRESPONSE,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryTasksResponse)
  })
_sym_db.RegisterMessage(QueryTasksResponse)

GetTaskParam = _reflection.GeneratedProtocolMessageType('GetTaskParam', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKPARAM,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.GetTaskParam)
  })
_sym_db.RegisterMessage(GetTaskParam)

ComputeTaskOutputAsset = _reflection.GeneratedProtocolMessageType('ComputeTaskOutputAsset', (_message.Message,), {
  'DESCRIPTOR' : _COMPUTETASKOUTPUTASSET,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.ComputeTaskOutputAsset)
  })
_sym_db.RegisterMessage(ComputeTaskOutputAsset)

ApplyTaskActionParam = _reflection.GeneratedProtocolMessageType('ApplyTaskActionParam', (_message.Message,), {
  'DESCRIPTOR' : _APPLYTASKACTIONPARAM,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.ApplyTaskActionParam)
  })
_sym_db.RegisterMessage(ApplyTaskActionParam)

ApplyTaskActionResponse = _reflection.GeneratedProtocolMessageType('ApplyTaskActionResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPLYTASKACTIONRESPONSE,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.ApplyTaskActionResponse)
  })
_sym_db.RegisterMessage(ApplyTaskActionResponse)

ComputeTaskInputAsset = _reflection.GeneratedProtocolMessageType('ComputeTaskInputAsset', (_message.Message,), {
  'DESCRIPTOR' : _COMPUTETASKINPUTASSET,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.ComputeTaskInputAsset)
  })
_sym_db.RegisterMessage(ComputeTaskInputAsset)

GetTaskInputAssetsParam = _reflection.GeneratedProtocolMessageType('GetTaskInputAssetsParam', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKINPUTASSETSPARAM,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.GetTaskInputAssetsParam)
  })
_sym_db.RegisterMessage(GetTaskInputAssetsParam)

GetTaskInputAssetsResponse = _reflection.GeneratedProtocolMessageType('GetTaskInputAssetsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKINPUTASSETSRESPONSE,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.GetTaskInputAssetsResponse)
  })
_sym_db.RegisterMessage(GetTaskInputAssetsResponse)

DisableOutputParam = _reflection.GeneratedProtocolMessageType('DisableOutputParam', (_message.Message,), {
  'DESCRIPTOR' : _DISABLEOUTPUTPARAM,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.DisableOutputParam)
  })
_sym_db.RegisterMessage(DisableOutputParam)

DisableOutputResponse = _reflection.GeneratedProtocolMessageType('DisableOutputResponse', (_message.Message,), {
  'DESCRIPTOR' : _DISABLEOUTPUTRESPONSE,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.DisableOutputResponse)
  })
_sym_db.RegisterMessage(DisableOutputResponse)

_COMPUTETASKSERVICE = DESCRIPTOR.services_by_name['ComputeTaskService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/substra/orchestrator/lib/asset'
  _COMPUTETASK_METADATAENTRY._options = None
  _COMPUTETASK_METADATAENTRY._serialized_options = b'8\001'
  _COMPUTETASK_OUTPUTSENTRY._options = None
  _COMPUTETASK_OUTPUTSENTRY._serialized_options = b'8\001'
  _NEWCOMPUTETASK_METADATAENTRY._options = None
  _NEWCOMPUTETASK_METADATAENTRY._serialized_options = b'8\001'
  _NEWCOMPUTETASK_OUTPUTSENTRY._options = None
  _NEWCOMPUTETASK_OUTPUTSENTRY._serialized_options = b'8\001'
  _COMPUTETASKCATEGORY._serialized_start=4303
  _COMPUTETASKCATEGORY._serialized_end=4431
  _COMPUTETASKSTATUS._serialized_start=4434
  _COMPUTETASKSTATUS._serialized_end=4585
  _COMPUTETASKACTION._serialized_start=4588
  _COMPUTETASKACTION._serialized_end=4727
  _PARENTTASKOUTPUTREF._serialized_start=144
  _PARENTTASKOUTPUTREF._serialized_end=217
  _COMPUTETASKINPUT._serialized_start=220
  _COMPUTETASKINPUT._serialized_end=351
  _COMPUTETASKOUTPUT._serialized_start=353
  _COMPUTETASKOUTPUT._serialized_end=439
  _NEWCOMPUTETASKOUTPUT._serialized_start=441
  _NEWCOMPUTETASKOUTPUT._serialized_end=533
  _COMPUTETASK._serialized_start=536
  _COMPUTETASK._serialized_end=1457
  _COMPUTETASK_METADATAENTRY._serialized_start=1321
  _COMPUTETASK_METADATAENTRY._serialized_end=1368
  _COMPUTETASK_OUTPUTSENTRY._serialized_start=1370
  _COMPUTETASK_OUTPUTSENTRY._serialized_end=1449
  _NEWCOMPUTETASK._serialized_start=1460
  _NEWCOMPUTETASK._serialized_end=2196
  _NEWCOMPUTETASK_METADATAENTRY._serialized_start=1321
  _NEWCOMPUTETASK_METADATAENTRY._serialized_end=1368
  _NEWCOMPUTETASK_OUTPUTSENTRY._serialized_start=2106
  _NEWCOMPUTETASK_OUTPUTSENTRY._serialized_end=2188
  _TRAINTASKDATA._serialized_start=2198
  _TRAINTASKDATA._serialized_end=2290
  _NEWTRAINTASKDATA._serialized_start=2292
  _NEWTRAINTASKDATA._serialized_end=2362
  _PREDICTTASKDATA._serialized_start=2364
  _PREDICTTASKDATA._serialized_end=2463
  _NEWPREDICTTASKDATA._serialized_start=2465
  _NEWPREDICTTASKDATA._serialized_end=2537
  _TESTTASKDATA._serialized_start=2539
  _TESTTASKDATA._serialized_end=2624
  _NEWTESTTASKDATA._serialized_start=2626
  _NEWTESTTASKDATA._serialized_end=2714
  _COMPOSITETRAINTASKDATA._serialized_start=2716
  _COMPOSITETRAINTASKDATA._serialized_end=2841
  _NEWCOMPOSITETRAINTASKDATA._serialized_start=2843
  _NEWCOMPOSITETRAINTASKDATA._serialized_end=2947
  _AGGREGATETRAINTASKDATA._serialized_start=2949
  _AGGREGATETRAINTASKDATA._serialized_end=2998
  _NEWAGGREGATETRAINTASKDATA._serialized_start=3000
  _NEWAGGREGATETRAINTASKDATA._serialized_end=3043
  _REGISTERTASKSPARAM._serialized_start=3045
  _REGISTERTASKSPARAM._serialized_end=3110
  _REGISTERTASKSRESPONSE._serialized_start=3112
  _REGISTERTASKSRESPONSE._serialized_end=3177
  _TASKQUERYFILTER._serialized_start=3180
  _TASKQUERYFILTER._serialized_end=3359
  _QUERYTASKSPARAM._serialized_start=3361
  _QUERYTASKSPARAM._serialized_end=3464
  _QUERYTASKSRESPONSE._serialized_start=3466
  _QUERYTASKSRESPONSE._serialized_end=3553
  _GETTASKPARAM._serialized_start=3555
  _GETTASKPARAM._serialized_end=3582
  _COMPUTETASKOUTPUTASSET._serialized_start=3585
  _COMPUTETASKOUTPUTASSET._serialized_end=3739
  _APPLYTASKACTIONPARAM._serialized_start=3741
  _APPLYTASKACTIONPARAM._serialized_end=3851
  _APPLYTASKACTIONRESPONSE._serialized_start=3853
  _APPLYTASKACTIONRESPONSE._serialized_end=3878
  _COMPUTETASKINPUTASSET._serialized_start=3881
  _COMPUTETASKINPUTASSET._serialized_end=4071
  _GETTASKINPUTASSETSPARAM._serialized_start=4073
  _GETTASKINPUTASSETSPARAM._serialized_end=4124
  _GETTASKINPUTASSETSRESPONSE._serialized_start=4126
  _GETTASKINPUTASSETSRESPONSE._serialized_end=4207
  _DISABLEOUTPUTPARAM._serialized_start=4209
  _DISABLEOUTPUTPARAM._serialized_end=4275
  _DISABLEOUTPUTRESPONSE._serialized_start=4277
  _DISABLEOUTPUTRESPONSE._serialized_end=4300
  _COMPUTETASKSERVICE._serialized_start=4730
  _COMPUTETASKSERVICE._serialized_end=5268
# @@protoc_insertion_point(module_scope)
