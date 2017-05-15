import threading

GLOBALS = threading.local()
GLOBALS.user = None  # type: django.contrib.auth.models.User
GLOBALS.request = None  # type: django.http.request.HttpRequest


def global_middleware(get_response):
    def middleware(request):
        # Accessing the __dict__ directly is specifically called out as a valid way
        # to interact with the local object in the _threading_local module documentation
        GLOBALS.__dict__.clear()
        GLOBALS.request = request
        GLOBALS.user = getattr(request, 'user', None)
        return get_response(request)

    return middleware
