# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
{% if cookiecutter.install_wagtail == "y" -%}
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls{% endif %}
from wagtail.documents import urls as wagtaildocs_urls

from .apps.core.urls import core
{%- if cookiecutter.install_allauth == "y" %}
from .apps.myauth.urls import myauth
from .apps.profile.urls import profile
{%- endif %}
from .contrib.health_check import health_check

urlpatterns = [
    url(r"^healthcheck/", health_check),
{%- if cookiecutter.install_rq == "y" %}
    url(r"^admin/django-rq/", include("django_rq.urls")),
{%- endif %}
    url(r"^admin/", admin.site.urls),
{%- if cookiecutter.install_allauth == "y" %}
    url(r"^", profile.urls),
{%- endif %}
    url(r"^home/", core.urls),
{%- if cookiecutter.install_wagtail == "y" %}
    url(r"^cms/", include(wagtailadmin_urls)),
    url(r"^documents/", include(wagtaildocs_urls)),
{%- endif %}
{%- if cookiecutter.install_allauth == "y" %}
    url(r"^auth/", myauth.urls),
{%- endif %}
]

if settings.DEBUG and getattr(settings, "USE_DEBUG_TOOLBAR", settings.DEBUG):  # pragma: no cover
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += [
        url(r"^__debug__/", include(debug_toolbar.urls)),
    ]

    # Dev static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

{% if cookiecutter.install_wagtail == "y" -%}
urlpatterns += [
    url(r"^", include(wagtail_urls)),
]
{% endif %}