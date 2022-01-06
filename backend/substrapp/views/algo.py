import tempfile

import structlog
from django.http import Http404
from django.urls import reverse
from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import GenericViewSet

import orchestrator.algo_pb2 as algo_pb2
from libs.pagination import DefaultPageNumberPagination
from libs.pagination import PaginationMixin
from substrapp.clients import node as node_client
from substrapp.models import Algo
from substrapp.orchestrator import get_orchestrator_client
from substrapp.serializers import AlgoSerializer
from substrapp.serializers import OrchestratorAlgoSerializer
from substrapp.utils import get_hash
from substrapp.views.filters_utils import filter_list
from substrapp.views.utils import ApiResponse
from substrapp.views.utils import PermissionMixin
from substrapp.views.utils import ValidationExceptionError
from substrapp.views.utils import get_channel_name
from substrapp.views.utils import node_has_process_permission
from substrapp.views.utils import validate_key

logger = structlog.get_logger(__name__)


def replace_storage_addresses(request, algo):
    algo["description"]["storage_address"] = request.build_absolute_uri(
        reverse("substrapp:algo-description", args=[algo["key"]])
    )
    algo["algorithm"]["storage_address"] = request.build_absolute_uri(
        reverse("substrapp:algo-file", args=[algo["key"]])
    )


class AlgoViewSet(mixins.CreateModelMixin, PaginationMixin, GenericViewSet):
    queryset = Algo.objects.all()
    serializer_class = AlgoSerializer
    pagination_class = DefaultPageNumberPagination

    def commit(self, serializer, request):
        # create on db
        instance = serializer.save()

        try:
            category = algo_pb2.AlgoCategory.Value(request.data.get("category"))
        except ValueError:
            instance.delete()  # warning: post delete signals are not executed by django rollback
            raise ValidationError({"category": "Invalid category"})

        # serialized data for orchestrator db
        orchestrator_serializer = OrchestratorAlgoSerializer(
            data={
                "name": request.data.get("name"),
                "category": category,
                "permissions": request.data.get("permissions"),
                "metadata": request.data.get("metadata"),
                "instance": instance,
            },
            context={"request": request},
        )
        if not orchestrator_serializer.is_valid():
            instance.delete()  # warning: post delete signals are not executed by django rollback
            raise ValidationError(orchestrator_serializer.errors)

        # create on orchestrator db
        try:
            data = orchestrator_serializer.create(get_channel_name(request), orchestrator_serializer.validated_data)
        except Exception:
            instance.delete()  # warning: post delete signals are not executed by django rollback
            raise

        merged_data = dict(serializer.data)
        merged_data.update(data)

        return merged_data

    def _create(self, request):
        file = request.data.get("file")
        try:
            checksum = get_hash(file)
        except Exception as e:
            raise ValidationExceptionError(e.args, "(not computed)", status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(
            data={"file": file, "description": request.data.get("description"), "checksum": checksum}
        )

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            raise ValidationExceptionError(e.args, "(not computed)", status.HTTP_400_BAD_REQUEST)
        else:
            return self.commit(serializer, request)

    def create(self, request, *args, **kwargs):
        data = self._create(request)
        headers = self.get_success_headers(data)
        return ApiResponse(data, status=status.HTTP_201_CREATED, headers=headers)

    def create_or_update_algo_description(self, channel_name, algo, key):
        # We need to have, at least, algo description for the frontend
        content = node_client.get(
            channel=channel_name,
            node_id=algo["owner"],
            url=algo["description"]["storage_address"],
            checksum=algo["description"]["checksum"],
        )

        description_file = tempfile.TemporaryFile()
        description_file.write(content)

        instance, created = Algo.objects.update_or_create(key=key)
        instance.description.save("description.md", description_file)

        return instance

    def _retrieve(self, request, key):
        validated_key = validate_key(key)

        with get_orchestrator_client(get_channel_name(request)) as client:
            data = client.query_algo(validated_key)

        # verify if algo description exists for the frontend view
        # if not fetch it if it's possible
        # do not fetch  algo description if node has not process permission
        if node_has_process_permission(data):
            try:
                instance = self.get_object()
            except Http404:
                instance = None
            finally:
                if not instance or not instance.description:
                    instance = self.create_or_update_algo_description(get_channel_name(request), data, validated_key)

                # For security reason, do not give access to local file address
                # Restrain data to some fields
                serializer = self.get_serializer(instance, fields=("owner"))
                data.update(serializer.data)

        replace_storage_addresses(request, data)

        return data

    def retrieve(self, request, *args, **kwargs):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        key = self.kwargs[lookup_url_kwarg]

        data = self._retrieve(request, key)
        return ApiResponse(data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        with get_orchestrator_client(get_channel_name(request)) as client:
            data = client.query_algos()

        query_params = request.query_params.get("search")

        if query_params is not None:
            data = filter_list(object_type="algo", data=data, query_params=query_params)

        for algo in data:
            replace_storage_addresses(request, algo)

        return self.paginate_response(data)


class AlgoPermissionViewSet(PermissionMixin, GenericViewSet):
    queryset = Algo.objects.all()
    serializer_class = AlgoSerializer

    @action(detail=True)
    def file(self, request, *args, **kwargs):
        return self.download_file(request, "query_algo", "file", "algorithm")

    # actions cannot be named "description"
    # https://github.com/encode/django-rest-framework/issues/6490
    # for some of the restricted names see:
    # https://www.django-rest-framework.org/api-guide/viewsets/#introspecting-viewset-actions
    @action(detail=True, url_path="description", url_name="description")
    def description_(self, request, *args, **kwargs):
        return self.download_file(request, "query_algo", "description")
