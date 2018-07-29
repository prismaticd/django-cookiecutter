# -*- coding: utf-8 -*-

from django.apps import AppConfig

from {{ cookiecutter.project_slug }}.contrib.seed_random import init_random


class CoreConfig(AppConfig):
    name = "{{ cookiecutter.project_slug }}.apps.core"

    def ready(self):
        init_random()
