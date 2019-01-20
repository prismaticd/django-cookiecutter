# -*- coding: utf-8 -*-

from .base_settings import *  # noqa
import os

DEBUG = False
MAIN_URL = "{{cookiecutter.prod_host}}"

{% if cookiecutter.database_type == "mysql" %}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
        "OPTIONS": {
            "charset": "utf8mb4",
            "init_command": "SET sql_mode='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'",
        },
        "TEST": {"CHARSET": "utf8mb4", "COLLATION": "utf8mb4_unicode_ci"},
    }
}
{% elif cookiecutter.database_type == "postgres" %}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}
{% endif %}



TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django_settings_export.settings_export",
            ],
            "loaders": [
                ("django.template.loaders.cached.Loader", [
                    "django.template.loaders.filesystem.Loader",
                    "django.template.loaders.app_directories.Loader",
                ])
            ]
        },
    },
]


ALLOWED_HOSTS = [MAIN_URL]
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEFAULT_FROM_EMAIL = "contact@{{cookiecutter.prod_host}}"

GTM_ID = ""
MEDIA_SECRET = os.environ.get("MEDIA_SECRET_KEY")

# Need absolute url for emails
STATIC_URL = "https://{}/static/".format(MAIN_URL)
