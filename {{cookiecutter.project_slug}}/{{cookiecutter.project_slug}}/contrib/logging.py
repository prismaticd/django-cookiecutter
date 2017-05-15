import logging
from {{cookiecutter.project_slug}}.contrib.request import GLOBALS
from django.conf import settings


# class ProjectLogHandler(logging.Handler):
#     def format_message(self, message):
#         message = super(ProjectLogHandler, self).format_message(message)
#
#         #  middleware is not called for static files so no attr user
#         if hasattr(GLOBALS, "user") and GLOBALS.user:
#             message['user_id'] = GLOBALS.user.id
#
#         message['log_level_int'] = self.level
#         message.update(settings.STATIC_LOGGING)
#
#         return message
