# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
{% if cookiecutter.install_wagtail == "y" %}
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls{% endif %}

from .apps.home.urls import home
from .contrib.health_check import health_check

urlpatterns = [
    url(r'^healthcheck/', health_check),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home.urls),
    {% if cookiecutter.install_wagtail == "y" %}
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),{% endif %}
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

    # Dev static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

{% if cookiecutter.install_wagtail == "y" %}
urlpatterns += [
    url(r'^', include(wagtail_urls)),
]{% endif %}