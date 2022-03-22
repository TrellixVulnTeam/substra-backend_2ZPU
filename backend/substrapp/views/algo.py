import structlog
from django.urls import reverse
from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import GenericViewSet

import orchestrator.algo_pb2 as algo_pb2
from libs.pagination import DefaultPageNumberPagination
from localrep.errors import AlreadyExistsError
from localrep.models import Algo as AlgoRep
from localrep.serializers import AlgoSerializer as AlgoRepSerializer
from substrapp.models import Algo
from substrapp.serializers import AlgoSerializer
from substrapp.serializers import OrchestratorAlgoSerializer
from substrapp.utils import get_hash
from substrapp.views.filters_utils import filter_queryset
from substrapp.views.utils import ApiResponse
from substrapp.views.utils import PermissionMixin
from substrapp.views.utils import ValidationExceptionError
from substrapp.views.utils import get_channel_name
from substrapp.views.utils import validate_key

logger = structlog.get_logger(__name__)


def replace_storage_addresses(request, algo):
    algo["description"]["storage_address"] = request.build_absolute_uri(
        reverse("substrapp:algo-description", args=[algo["key"]])
    )
    algo["algorithm"]["storage_address"] = request.build_absolute_uri(
        reverse("substrapp:algo-file", args=[algo["key"]])
    )


class AlgoListMixin:
    def list(self, request, compute_plan_pk=None):
        queryset = AlgoRep.objects.filter(channel=get_channel_name(request)).order_by("creation_date", "key")

        if compute_plan_pk is not None:
            validated_key = validate_key(compute_plan_pk)
            queryset = queryset.filter(compute_tasks__compute_plan__key=validated_key).distinct()

        query_params = request.query_params.get("search")
        if query_params is not None:

            def map_category(key, values):
                if key == "category":
                    values = [algo_pb2.AlgoCategory.Value(value) for value in values]
                return key, values

            queryset = filter_queryset("algo", queryset, query_params, mapping_callback=map_category)
        queryset = self.paginate_queryset(queryset)

        data = AlgoRepSerializer(queryset, many=True).data
        for algo in data:
            replace_storage_addresses(request, algo)

        return self.get_paginated_response(data)


class CPAlgoViewSet(AlgoListMixin, GenericViewSet):
    pagination_class = DefaultPageNumberPagination

    def get_queryset(self):
        return []


class AlgoViewSet(AlgoListMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Algo.objects.all()
    serializer_class = AlgoSerializer
    pagination_class = DefaultPageNumberPagination

    def _register_in_orchestrator(self, request, instance):
        """Register algo in orchestrator."""
        try:
            category = algo_pb2.AlgoCategory.Value(request.data.get("category"))
        except ValueError:
            raise ValidationError({"category": "Invalid category"})

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
        orchestrator_serializer.is_valid(raise_exception=True)
        return orchestrator_serializer.create(get_channel_name(request), orchestrator_serializer.validated_data)

    def _create(self, request):
        """Create a new algo.

        The workflow is composed of several steps:
        - Save files in local database to get the addresses.
        - Register asset in the orchestrator.
        - Save metadata in local database.
        """
        # Step1: save files in local database
        file = request.data.get("file")
        try:
            checksum = get_hash(file)
        except Exception as e:
            raise ValidationExceptionError(e.args, "(not computed)", status.HTTP_400_BAD_REQUEST)

        serializer = AlgoSerializer(
            data={"file": file, "description": request.data.get("description"), "checksum": checksum}
        )

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            raise ValidationExceptionError(e.args, "(not computed)", status.HTTP_400_BAD_REQUEST)

        instance = serializer.save()

        # Step2: register asset in orchestrator
        try:
            localrep_data = self._register_in_orchestrator(request, instance)
        except Exception:
            instance.delete()  # warning: post delete signals are not executed by django rollback
            raise

        # Step3: save metadata in local database
        localrep_data["channel"] = get_channel_name(request)
        localrep_serializer = AlgoRepSerializer(data=localrep_data)
        try:
            localrep_serializer.save_if_not_exists()
        except AlreadyExistsError:
            # May happen if the events app already processed the event pushed by the orchestrator
            algo = AlgoRep.objects.get(key=localrep_data["key"])
            data = AlgoRepSerializer(algo).data
        except Exception:
            instance.delete()  # warning: post delete signals are not executed by django rollback
            raise
        else:
            data = localrep_serializer.data

        # Returns algo metadata from local database (and algo data) to ensure consistency between GET and CREATE views
        data.update(serializer.data)
        return data

    def create(self, request, *args, **kwargs):
        data = self._create(request)
        headers = self.get_success_headers(data)
        return ApiResponse(data, status=status.HTTP_201_CREATED, headers=headers)

    def _retrieve(self, request, key):
        validated_key = validate_key(key)
        try:
            algo = AlgoRep.objects.filter(channel=get_channel_name(request)).get(key=validated_key)
        except AlgoRep.DoesNotExist:
            raise NotFound
        data = AlgoRepSerializer(algo).data

        replace_storage_addresses(request, data)

        return data

    def retrieve(self, request, *args, **kwargs):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        key = self.kwargs[lookup_url_kwarg]
        data = self._retrieve(request, key)
        return ApiResponse(data, status=status.HTTP_200_OK)


class AlgoPermissionViewSet(PermissionMixin, GenericViewSet):
    queryset = Algo.objects.all()
    serializer_class = AlgoSerializer

    @action(detail=True)
    def file(self, request, *args, **kwargs):
        return self.download_file(request, AlgoRep, "file", "algorithm_address")

    # actions cannot be named "description"
    # https://github.com/encode/django-rest-framework/issues/6490
    # for some of the restricted names see:
    # https://www.django-rest-framework.org/api-guide/viewsets/#introspecting-viewset-actions
    @action(detail=True, url_path="description", url_name="description")
    def description_(self, request, *args, **kwargs):
        return self.download_file(request, AlgoRep, "description", "description_address")
