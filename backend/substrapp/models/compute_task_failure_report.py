import urllib.parse
import uuid
from typing import Final

from django.conf import settings
from django.db import models

LOGS_BASE_PATH: Final[str] = "logs"
LOGS_FILE_PATH: Final[str] = "file"

_UUID_STRING_REPR_LENGTH: Final[int] = 36
_SHA256_STRING_REPR_LENGTH: Final[int] = 256 // 4


def _upload_to(instance: "ComputeTaskFailureReport", _filename: str) -> str:
    return str(instance.compute_task_key)


class ComputeTaskFailureReport(models.Model):
    """Store information relative to a compute task."""

    compute_task_key = models.UUIDField(primary_key=True, editable=False)
    logs = models.FileField(
        storage=settings.COMPUTE_TASK_LOGS_STORAGE, max_length=_UUID_STRING_REPR_LENGTH, upload_to=_upload_to
    )
    logs_checksum = models.CharField(max_length=_SHA256_STRING_REPR_LENGTH)
    creation_date = models.DateTimeField(auto_now_add=True)

    @property
    def key(self) -> uuid.UUID:
        return self.compute_task_key

    @property
    def logs_address(self) -> str:
        logs_path = f"{LOGS_BASE_PATH}/{self.compute_task_key}/{LOGS_FILE_PATH}/"
        return urllib.parse.urljoin(settings.DEFAULT_DOMAIN, logs_path)
