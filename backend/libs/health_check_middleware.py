import structlog
from django.conf import settings
from django.http import HttpResponse

from localrep.models import ChannelNode as ChannelNodeRep
from substrapp.orchestrator import get_orchestrator_client

logger = structlog.get_logger(__name__)


class HealthCheckMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.method == "GET":
            if request.path == "/readiness":
                return self.readiness(request)
            elif request.path == "/liveness":
                return self.liveness(request)
        return self.get_response(request)

    def liveness(self, request):
        """
        Returns that the server is alive.
        """
        validate_connections()

        validate_channels()

        return HttpResponse("OK")

    def readiness(self, request):
        """
        Returns that the server is alive.
        """
        validate_connections()

        validate_channels()

        return HttpResponse("OK")


def validate_connections():
    if not settings.ISOLATED:
        # Check orchestrator connection for each channel
        for channel_name, channel_settings in settings.LEDGER_CHANNELS.items():
            with get_orchestrator_client(channel_name) as client:
                client.query_version()


def validate_channels():
    # Check channel restrictions
    for channel_name, channel_settings in settings.LEDGER_CHANNELS.items():
        nodes = ChannelNodeRep.objects.filter(channel=channel_name).values_list("node_id", flat=True)

        # throw an Exception if the solo channel has more than 1 member
        if channel_name.startswith("solo-") or channel_settings["restricted"]:
            if len(nodes) > 1:
                raise Exception(
                    f"Restricted channel {channel_name} should have at most 1 member, but has " f"{len(nodes)}"
                )

        # throw an Exception if the node is not in the list
        if settings.LEDGER_MSP_ID not in nodes:
            raise Exception(f'Node {settings.LEDGER_MSP_ID} is not registered in channel "{channel_name}"')
