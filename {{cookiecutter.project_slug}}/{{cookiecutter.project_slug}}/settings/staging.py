# -*- coding: utf-8 -*-

from .base_settings import *  # noqa
import os

DEBUG = False
MAIN_URL = '{{cookiecutter.staging_host}}'

{% if cookiecutter.database_type == "mysql" %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),
    }
}
{% elif cookiecutter.database_type == "postgres" %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),
    }
}
{% endif %}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ])
            ]
        },
    },
]


ALLOWED_HOSTS = [MAIN_URL]
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEFAULT_FROM_EMAIL = "contact@{{cookiecutter.staging_host}}"

GTM_ID = ""
MEDIA_SECRET = os.environ.get("MEDIA_SECRET_KEY")

# Need absolute url for emails
STATIC_URL = "https://{}/static/".format(MAIN_URL)
