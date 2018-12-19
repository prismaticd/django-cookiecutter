from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.http.request import HttpRequest
from django.urls import reverse


class GeneratedEmailMissingException(Exception):
    pass


class ProfileMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # type: (HttpRequest) -> HttpResponseRedirect
        to_avoid = any(url not in str(request.path) for url in [reverse("profile:edit"), "logout", "cms", "admin"])
        if request.user.is_authenticated and not to_avoid:
            try:
                profile = request.user.profile
            except (ObjectDoesNotExist, GeneratedEmailMissingException):
                return HttpResponseRedirect(reverse("profile:edit"))

        return self.get_response(request)
