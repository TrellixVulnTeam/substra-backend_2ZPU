import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=os.environ.get("RAVEN_URL", "https://cff352ba26fc49f19e01692db93bf951@sentry.io/1317743"),
    integrations=[DjangoIntegration()]
)
