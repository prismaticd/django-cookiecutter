# -*- coding: utf-8 -*-

import logging

from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)


class HomePageView(TemplateView):
    template_name = "core/home_page.html"
