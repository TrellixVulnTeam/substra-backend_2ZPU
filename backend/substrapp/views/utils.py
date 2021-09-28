import os
import uuid

from django.http import FileResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings

from node.authentication import NodeUser
from substrapp.utils import get_remote_file, get_owner, get_remote_file_content
from node.models import OutgoingNode

from rest_framework import status
from requests.auth import HTTPBasicAuth
from wsgiref.util import is_hop_by_hop

from substrapp.exceptions import AssetPermissionError, NodeError, BadRequestError
import substrapp.orchestrator.computetask_pb2 as computetask_pb2
import substrapp.orchestrator.model_pb2 as model_pb2
from substrapp.orchestrator.api import get_orchestrator_client
from substrapp.orchestrator.error import OrcError


TASK_CATEGORY = {
    'unknown': computetask_pb2.TASK_UNKNOWN,
    'traintuple': computetask_pb2.TASK_TRAIN,
    'testtuple': computetask_pb2.TASK_TEST,
    'aggregatetuple': computetask_pb2.TASK_AGGREGATE,
    'composite_traintuple': computetask_pb2.TASK_COMPOSITE
}

TASK_FIELD = {
    'traintuple': 'train',
    'testtuple': 'test',
    'aggregatetuple': 'aggregate',
    'composite_traintuple': 'composite'
}


MODEL_CATEGORY = {
    'unknown': model_pb2.MODEL_UNKNOWN,
    'simple': model_pb2.MODEL_SIMPLE,
    'head': model_pb2.MODEL_HEAD,
}


HTTP_HEADER_PROXY_ASSET = "Substra-Proxy-Asset"


def authenticate_outgoing_request(outgoing_node_id):
    try:
        outgoing = OutgoingNode.objects.get(node_id=outgoing_node_id)
    except OutgoingNode.DoesNotExist:
        raise NodeError(
            f"Unauthorized to call remote node with node_id: {outgoing_node_id}"
        )

    # to authenticate to remote node we use the current node id
    # with the associated outgoing secret.
    current_node_id = get_owner()

    return HTTPBasicAuth(current_node_id, outgoing.secret)


def get_remote_asset(channel_name, url, node_id, content_checksum, salt=None):
    auth = authenticate_outgoing_request(node_id)
    return get_remote_file_content(channel_name, url, auth, content_checksum, salt=salt)


class CustomFileResponse(FileResponse):
    def set_headers(self, filelike):
        super(CustomFileResponse, self).set_headers(filelike)

        self["Access-Control-Expose-Headers"] = "Content-Disposition"


def node_has_process_permission(asset):
    """Check if current node can process input asset."""
    permission = asset["permissions"]["process"]
    return permission["public"] or get_owner() in permission["authorized_ids"]


class PermissionMixin(object):
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES + [
        BasicAuthentication
    ]
    permission_classes = [IsAuthenticated]

    def check_access(
        self, channel_name: str, user, asset, is_proxied_request: bool
    ) -> None:
        """Returns true if API consumer is allowed to access data.

        :param is_proxied_request: True if the API consumer is another backend-server proxying a user request
        :raises: AssetPermissionError
        """
        if user.is_anonymous:  # safeguard, should never happened
            raise AssetPermissionError()

        if type(user) is NodeUser:  # for node
            permission = asset["permissions"]["process"]
            node_id = user.username
        else:
            # for classic user, test on current msp id
            # TODO: This should be 'download' instead of 'process',
            #       but 'download' is not consistently exposed by chaincode yet.
            permission = asset["permissions"]["process"]
            node_id = get_owner()

        if not permission["public"] and node_id not in permission["authorized_ids"]:
            raise AssetPermissionError()

    def get_storage_address(self, asset, ledger_field) -> str:
        return asset[ledger_field]["storage_address"]

    def download_file(
        self, request, query_method, django_field, orchestrator_field=None
    ):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        key = self.kwargs[lookup_url_kwarg]
        channel_name = get_channel_name(request)

        validate_key(key)

        try:
            with get_orchestrator_client(get_channel_name(request)) as client:
                asset = getattr(client, query_method)(key)
        except OrcError as rpc_error:
            return Response(
                {"message": rpc_error.details}, status=rpc_error.http_status()
            )

        try:
            self.check_access(
                channel_name, request.user, asset, is_proxied_request(request)
            )
        except AssetPermissionError as e:
            return Response({"message": str(e)}, status=status.HTTP_403_FORBIDDEN)

        if get_owner() == asset["owner"]:
            response = self.get_local_file_response(django_field)
        else:
            if not orchestrator_field:
                orchestrator_field = django_field
            storage_address = self.get_storage_address(asset, orchestrator_field)
            response = self._download_remote_file(channel_name, storage_address, asset)

        return response

    def download_local_file(
        self, request, query_method, django_field, orchestrator_field=None
    ):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        key = self.kwargs[lookup_url_kwarg]

        validate_key(key)

        try:
            with get_orchestrator_client(get_channel_name(request)) as client:
                asset = getattr(client, query_method)(key)
        except OrcError as rpc_error:
            return Response(
                {"message": rpc_error.details}, status=rpc_error.http_status()
            )

        try:
            self.check_access(
                get_channel_name(request),
                request.user,
                asset,
                is_proxied_request(request),
            )
        except AssetPermissionError as e:
            return Response({"message": str(e)}, status=status.HTTP_403_FORBIDDEN)

        if not orchestrator_field:
            orchestrator_field = django_field

        return self.get_local_file_response(django_field)

    def get_local_file_response(self, django_field):
        obj = self.get_object()
        data = getattr(obj, django_field)
        response = CustomFileResponse(
            open(data.path, "rb"),
            as_attachment=True,
            filename=os.path.basename(data.path),
        )
        return response

    def _download_remote_file(self, channel_name, storage_address, asset):
        node_id = asset["owner"]
        auth = authenticate_outgoing_request(node_id)

        r = get_remote_file(
            channel_name,
            storage_address,
            auth,
            stream=True,
            headers={HTTP_HEADER_PROXY_ASSET: "True"},
        )

        if not r.ok:
            return Response(
                {
                    "message": f'Cannot proxify asset from node {asset["owner"]}: {str(r.text)}'
                },
                status=r.status_code,
            )

        response = CustomFileResponse(
            streaming_content=(chunk for chunk in r.iter_content(512 * 1024)),
            status=r.status_code,
        )

        for header in r.headers:
            # We don't use hop_by_hop headers since they are incompatible
            # with WSGI
            if not is_hop_by_hop(header):
                response[header] = r.headers.get(header)

        return response


def validate_key(key):
    try:
        uuid.UUID(key)
    except ValueError:
        raise BadRequestError(f'key is not a valid UUID: "{key}"')


def validate_sort(sort):
    if sort not in ["asc", "desc"]:
        raise BadRequestError(
            f"Invalid sort value (must be either 'desc' or 'asc'): {sort}"
        )


class ValidationExceptionError(Exception):
    def __init__(self, data, key, st):
        self.data = data
        self.key = key
        self.st = st
        super(ValidationExceptionError).__init__()


def get_channel_name(request):

    if hasattr(request.user, "channel"):
        return request.user.channel.name

    if "Substra-Channel-Name" in request.headers:
        return request.headers["Substra-Channel-Name"]

    raise BadRequestError("Could not determine channel name")


def is_proxied_request(request) -> bool:
    """Return True if the API consumer is another backend-server node proxying a user request.

    :param request: incoming HTTP request
    """
    return HTTP_HEADER_PROXY_ASSET in request.headers


def add_task_extra_information(client, basename, data):
    # add model information on a training compute task or performance on a testing compute task
    if basename in ['traintuple', 'aggregatetuple', 'composite_traintuple']:
        if computetask_pb2.ComputeTaskStatus.Value(data['status']) == computetask_pb2.STATUS_DONE:
            data[TASK_FIELD[basename]]['models'] = client.get_computetask_output_models(data['key'])
    elif basename in ['testtuple']:
        if computetask_pb2.ComputeTaskStatus.Value(data['status']) == computetask_pb2.STATUS_DONE:
            performance = client.get_compute_task_performance(data['key'])['performance_value']
            data[TASK_FIELD[basename]]['perf'] = performance

    return data
