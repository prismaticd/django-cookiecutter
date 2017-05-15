from django.http import JsonResponse
from django.contrib.auth.models import User


def health_check(request):
    a = User.objects.first()
    if a:
        db = "ok"
    else:
        db = "ko"

    return JsonResponse({"db":db})