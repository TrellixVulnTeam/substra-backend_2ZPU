"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import computetask_pb2
import grpc

class ComputeTaskServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    RegisterTasks: grpc.UnaryUnaryMultiCallable[
        computetask_pb2.RegisterTasksParam,
        computetask_pb2.RegisterTasksResponse] = ...

    QueryTasks: grpc.UnaryUnaryMultiCallable[
        computetask_pb2.QueryTasksParam,
        computetask_pb2.QueryTasksResponse] = ...

    GetTask: grpc.UnaryUnaryMultiCallable[
        computetask_pb2.GetTaskParam,
        computetask_pb2.ComputeTask] = ...

    ApplyTaskAction: grpc.UnaryUnaryMultiCallable[
        computetask_pb2.ApplyTaskActionParam,
        computetask_pb2.ApplyTaskActionResponse] = ...


class ComputeTaskServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def RegisterTasks(self,
        request: computetask_pb2.RegisterTasksParam,
        context: grpc.ServicerContext,
    ) -> computetask_pb2.RegisterTasksResponse: ...

    @abc.abstractmethod
    def QueryTasks(self,
        request: computetask_pb2.QueryTasksParam,
        context: grpc.ServicerContext,
    ) -> computetask_pb2.QueryTasksResponse: ...

    @abc.abstractmethod
    def GetTask(self,
        request: computetask_pb2.GetTaskParam,
        context: grpc.ServicerContext,
    ) -> computetask_pb2.ComputeTask: ...

    @abc.abstractmethod
    def ApplyTaskAction(self,
        request: computetask_pb2.ApplyTaskActionParam,
        context: grpc.ServicerContext,
    ) -> computetask_pb2.ApplyTaskActionResponse: ...


def add_ComputeTaskServiceServicer_to_server(servicer: ComputeTaskServiceServicer, server: grpc.Server) -> None: ...
