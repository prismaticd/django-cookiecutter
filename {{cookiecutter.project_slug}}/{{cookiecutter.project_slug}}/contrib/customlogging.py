import logging

from django.conf import settings

from .request import GLOBALS


class GrayFilter(logging.Filter):  # pragma: no cover
    def filter(self, record):
        # check for request._cached_user before accessing the user object,
        # this means django.contrib.auth.middleware.get_user has returned.
        # This avoid hitting a recursive loop when the "django" logger level = "DEBUG".
        if hasattr(GLOBALS.request, "_cached_user") and hasattr(GLOBALS, "user") and GLOBALS.user:
            record.user_id = GLOBALS.user.id

        record.env = settings.STATIC_LOGGING.get("env")

        return True
