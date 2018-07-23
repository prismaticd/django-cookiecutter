# -*- coding: utf-8 -*-

import logging

from django.conf.urls import url

from . import views

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ProfileApp(object):
    name = "profile_app"

    def get_urls(self):
        urlpatterns = [url(r"^profile/$", views.MyProfileView.as_view(), name="edit")]
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls(), self.name, "profile"


profile = ProfileApp()
