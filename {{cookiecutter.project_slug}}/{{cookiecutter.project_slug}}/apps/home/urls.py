# -*- coding: utf-8 -*-

import logging

from django.conf.urls import url

from .views import HomePageView

# Get an instance of a logger
logger = logging.getLogger(__name__)


class HomeApp(object):
    name = "home_app"

    def get_urls(self):
        urlpatterns = [
            url(r'$', HomePageView.as_view(), name='home-page'),
        ]
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls(), 'home_app', self.name


home = HomeApp()
