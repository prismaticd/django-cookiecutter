# -*- coding: utf-8 -*-

import logging

from django.conf.urls import url

from .views import HomePageView

# Get an instance of a logger
logger = logging.getLogger(__name__)


class CoreApp(object):
    name = "core"

    def get_urls(self):
        urlpatterns = [url(r"$", HomePageView.as_view(), name="home-page")]
        return urlpatterns

    @property
    def urls(self):
        # as per django.contrib.admin.sites.AdminSite#urls
        return self.get_urls(), "core", self.name


core = CoreApp()
