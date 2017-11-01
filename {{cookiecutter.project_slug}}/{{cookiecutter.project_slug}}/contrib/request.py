from threading import local
from django.contrib.auth import models
from django.http.request import HttpRequest


class MyGolbals(local):
    def __init__(self):
        self.user = None  # type: models.User
        self.request = None  # type: HttpRequest

    def reset(self):
        self.user = None
        self.request = None


GLOBALS = MyGolbals()


def global_middleware(get_response):
    def middleware(request: HttpRequest):
        # Accessing the __dict__ directly is specifically called out as a valid way
        # to interact with the local object in the _threading_local module documentation
        GLOBALS.reset()
        GLOBALS.request = request
        GLOBALS.user = getattr(request, 'user', None)
        return get_response(request)

    return middleware
