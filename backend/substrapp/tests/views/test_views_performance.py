import os
import shutil
import tempfile

from django.test import override_settings
from django.urls import reverse
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.test import APITestCase

import orchestrator.computeplan_pb2 as computeplan_pb2
import orchestrator.computetask_pb2 as computetask_pb2
from localrep.models import Performance as PerformanceRep
from substrapp.tests import factory

from ..common import AuthenticatedClient

MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(
    MEDIA_ROOT=MEDIA_ROOT, LEDGER_CHANNELS={"mychannel": {"chaincode": {"name": "mycc"}, "model_export_enabled": True}}
)
class CPPerformanceViewTests(APITestCase):
    client_class = AuthenticatedClient

    def setUp(self):
        if not os.path.exists(MEDIA_ROOT):
            os.makedirs(MEDIA_ROOT)

        self.algo = factory.create_algo()
        self.data_manager = factory.create_datamanager()
        self.data_sample = factory.create_datasample([self.data_manager])
        self.compute_plan = factory.create_computeplan()

        self.extra = {"HTTP_SUBSTRA_CHANNEL_NAME": "mychannel", "HTTP_ACCEPT": "application/json;version=0.0"}
        self.url = reverse("substrapp:compute_plan_perf-list", args=[self.compute_plan.key])

        self.metrics = [factory.create_metric() for _ in range(3)]
        self.compute_task = factory.create_computetask(
            self.compute_plan,
            algo=self.algo,
            metrics=self.metrics,
            data_manager=self.data_manager,
            data_samples=[self.data_sample.key],
            category=computetask_pb2.TASK_TEST,
            status=computetask_pb2.STATUS_DONE,
            error_type=None,
        )
        self.performances = [factory.create_performance(self.compute_task, self.metrics[i]) for i in range(3)]
        self.expected_results = [
            {
                "compute_task": {
                    "key": str(self.compute_task.key),
                    "data_manager_key": str(self.data_manager.key),
                    "algo_key": str(self.algo.key),
                    "rank": 1,
                    "round_idx": None,
                    "data_samples": [str(self.data_sample.key)],
                    "worker": "MyOrg1MSP",
                },
                "metric": {
                    "key": str(self.metrics[0].key),
                    "name": self.metrics[0].name,
                },
                "perf": self.performances[0].value,
            },
            {
                "compute_task": {
                    "key": str(self.compute_task.key),
                    "data_manager_key": str(self.data_manager.key),
                    "algo_key": str(self.algo.key),
                    "rank": 1,
                    "round_idx": None,
                    "data_samples": [str(self.data_sample.key)],
                    "worker": "MyOrg1MSP",
                },
                "metric": {
                    "key": str(self.metrics[1].key),
                    "name": self.metrics[1].name,
                },
                "perf": self.performances[1].value,
            },
            {
                "compute_task": {
                    "key": str(self.compute_task.key),
                    "data_manager_key": str(self.data_manager.key),
                    "algo_key": str(self.algo.key),
                    "rank": 1,
                    "round_idx": None,
                    "data_samples": [str(self.data_sample.key)],
                    "worker": "MyOrg1MSP",
                },
                "metric": {
                    "key": str(self.metrics[2].key),
                    "name": self.metrics[2].name,
                },
                "perf": self.performances[2].value,
            },
        ]

    def tearDown(self):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)

    def test_performance_list_empty(self):
        PerformanceRep.objects.all().delete()
        response = self.client.get(self.url, **self.extra)
        self.assertEqual(response.json(), {"count": 0, "next": None, "previous": None, "results": []})

    def test_performance_list(self):
        response = self.client.get(self.url, **self.extra)
        self.assertEqual(
            response.json(),
            {"count": len(self.expected_results), "next": None, "previous": None, "results": self.expected_results},
        )


class PerformanceViewTests(APITestCase):
    client_class = AuthenticatedClient

    def setUp(self):
        if not os.path.exists(MEDIA_ROOT):
            os.makedirs(MEDIA_ROOT)

        self.maxDiff = None
        self.algo = factory.create_algo()
        self.data_manager = factory.create_datamanager()
        self.data_sample = factory.create_datasample([self.data_manager])
        self.compute_plans = [
            factory.create_computeplan(status=computeplan_pb2.PLAN_STATUS_DOING),
            factory.create_computeplan(status=computeplan_pb2.PLAN_STATUS_DONE),
        ]

        self.extra = {"HTTP_SUBSTRA_CHANNEL_NAME": "mychannel", "HTTP_ACCEPT": "application/json;version=0.0"}
        self.url = reverse("substrapp:performance-list")
        self.export_extra = {"HTTP_SUBSTRA_CHANNEL_NAME": "mychannel", "HTTP_ACCEPT": "*/*"}
        self.export_url = reverse("substrapp:performance-export")

        self.metrics = [factory.create_metric() for _ in range(3)]
        self.compute_tasks = [
            factory.create_computetask(
                self.compute_plans[i],
                algo=self.algo,
                metrics=self.metrics,
                data_manager=self.data_manager,
                data_samples=[self.data_sample.key],
                category=computetask_pb2.TASK_TEST,
                status=computetask_pb2.STATUS_DONE,
                error_type=None,
            )
            for i in range(2)
        ]
        self.performances = [factory.create_performance(self.compute_tasks[0], self.metrics[i]) for i in range(3)]
        self.performances.extend([factory.create_performance(self.compute_tasks[1], self.metrics[i]) for i in range(3)])
        self.expected_results = [
            {
                "compute_plan_key": self.compute_plans[0],
                "compute_plan_name": None,
                "compute_plan_tag": "",
                "compute_plan_status": "PLAN_STATUS_TODO",
                "compute_plan_start_date": None,
                "compute_plan_end_date": None,
                "compute_plan_metadata": {},
                "compute_task__metadata": {},
                "metric_name": "metric",
                "worker": "MyOrg1MSP",
                "test_task_rank": 1,
                "test_task_round": None,
                "performance": 1.0,
            },
            {
                "compute_plan_key": self.compute_plans[0],
                "compute_plan_name": None,
                "compute_plan_tag": "",
                "compute_plan_status": "PLAN_STATUS_TODO",
                "compute_plan_start_date": None,
                "compute_plan_end_date": None,
                "compute_plan_metadata": {},
                "compute_task__metadata": {},
                "metric_name": "metric",
                "worker": "MyOrg1MSP",
                "test_task_rank": 1,
                "test_task_round": None,
                "performance": 1.0,
            },
            {
                "compute_plan_key": self.compute_plans[0],
                "compute_plan_name": None,
                "compute_plan_tag": "",
                "compute_plan_status": "PLAN_STATUS_TODO",
                "compute_plan_start_date": None,
                "compute_plan_end_date": None,
                "compute_plan_metadata": {},
                "compute_task__metadata": {},
                "metric_name": "metric",
                "worker": "MyOrg1MSP",
                "test_task_rank": 1,
                "test_task_round": None,
                "performance": 1.0,
            },
            {
                "compute_plan_key": self.compute_plans[1],
                "compute_plan_name": None,
                "compute_plan_tag": "",
                "compute_plan_status": "PLAN_STATUS_TODO",
                "compute_plan_start_date": None,
                "compute_plan_end_date": None,
                "compute_plan_metadata": {},
                "compute_task__metadata": {},
                "metric_name": "metric",
                "worker": "MyOrg1MSP",
                "test_task_rank": 1,
                "test_task_round": None,
                "performance": 1.0,
            },
            {
                "compute_plan_key": self.compute_plans[1],
                "compute_plan_name": None,
                "compute_plan_tag": "",
                "compute_plan_status": "PLAN_STATUS_TODO",
                "compute_plan_start_date": None,
                "compute_plan_end_date": None,
                "compute_plan_metadata": {},
                "compute_task__metadata": {},
                "metric_name": "metric",
                "worker": "MyOrg1MSP",
                "test_task_rank": 1,
                "test_task_round": None,
                "performance": 1.0,
            },
            {
                "compute_plan_key": self.compute_plans[1],
                "compute_plan_name": None,
                "compute_plan_tag": "",
                "compute_plan_status": "PLAN_STATUS_TODO",
                "compute_plan_start_date": None,
                "compute_plan_end_date": None,
                "compute_plan_metadata": {},
                "compute_task__metadata": {},
                "metric_name": "metric",
                "worker": "MyOrg1MSP",
                "test_task_rank": 1,
                "test_task_round": None,
                "performance": 1.0,
            },
        ]

    def tearDown(self):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)

    def test_performance_view(self):
        response = self.client.get(self.url, **self.extra)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performance_export(self):
        response = self.client.get(self.export_url, **self.export_extra)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(list(response.streaming_content)), len(self.expected_results) + 1)

    def test_performance_export_with_metadata(self):
        metadata = "epochs,hidden_sizes,last_hidden_sizes"
        params = urlencode({"metadata": metadata})
        response = self.client.get(f"{self.export_url}?{params}", **self.export_extra)
        content_list = list(response.streaming_content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(metadata in str(content_list[0]))
        self.assertEqual(len(content_list), len(self.expected_results) + 1)

    def test_performance_export_filter(self):
        """Filter performance on cp key."""
        key = self.compute_plans[0].key
        params = urlencode({"key": key})
        response = self.client.get(f"{self.export_url}?{params}", **self.export_extra)
        content_list = list(response.streaming_content)
        self.assertEqual(len(content_list), 4)
        self.assertTrue(str(self.compute_plans[0].key) in str(content_list[1]))

    def test_performance_export_filter_in(self):
        """Filter performance on cp in key_0, key_1."""
        key_0 = self.compute_plans[0].key
        key_1 = self.compute_plans[1].key
        params = urlencode({"key": ",".join([str(key_0), str(key_1)])})
        response = self.client.get(f"{self.export_url}?{params}", **self.export_extra)
        content_list = list(response.streaming_content)
        self.assertEqual(len(content_list), len(self.expected_results) + 1)

    def test_performance_export_filter_and(self):
        """Filter performance on cp key and status."""
        key_0 = self.compute_plans[0].key
        key_1 = self.compute_plans[1].key
        status = computeplan_pb2.ComputePlanStatus.Name(computeplan_pb2.PLAN_STATUS_DOING)
        params = urlencode({"key": ",".join([str(key_0), str(key_1)]), "status": status})
        response = self.client.get(f"{self.export_url}?{params}", **self.export_extra)
        content_list = list(response.streaming_content)
        self.assertEqual(len(content_list), 4)
        self.assertTrue(status in str(content_list[1]))
