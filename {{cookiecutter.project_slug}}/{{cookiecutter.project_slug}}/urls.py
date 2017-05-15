# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from .apps.home.urls import home
from .contrib.health_check import health_check

urlpatterns = [
    url(r'^healthcheck/', health_check),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home.urls),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

    # Dev static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

