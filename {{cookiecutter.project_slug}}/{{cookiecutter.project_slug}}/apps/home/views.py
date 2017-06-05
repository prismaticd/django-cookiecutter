# -*- coding: utf-8 -*-

import logging
from django.views.generic.base import TemplateView
from .apps import HomeConfig

logger = logging.getLogger(__name__)


class HomePageView(TemplateView):
    template_name = "home/home.html"
