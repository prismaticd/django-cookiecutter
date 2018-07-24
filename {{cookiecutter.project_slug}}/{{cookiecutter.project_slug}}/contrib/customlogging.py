from .request import GLOBALS
from django.conf import settings
import logging


class GrayFilter(logging.Filter):  # pragma: no cover

    def filter(self, record):
        if hasattr(GLOBALS, "user") and GLOBALS.user:
            record.user_id = GLOBALS.user.id

        record.env = settings.STATIC_LOGGING.get("env")

        return True
