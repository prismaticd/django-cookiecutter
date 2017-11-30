# -*- coding: utf-8 -*-

from .base_settings import *  # noqa
import os

{% if cookiecutter.database_type == "mysql" %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("MYSQL_DATABASE", "{{cookiecutter.project_slug}}"),
        'USER': os.environ.get("DB_USER", "root"),
        'PASSWORD': os.environ.get("MYSQL_ROOT_PASSWORD"),
        'HOST': os.environ.get("DB_HOST", "127.0.0.1"),
        'PORT': os.environ.get("DB_PORT", "3306"),
    }
}
{% elif cookiecutter.database_type == "postgres" %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DB", 'postgres'),
        'USER': os.environ.get("POSTGRES_USER", 'postgres'),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD", ''),
        'HOST': os.environ.get("DB_HOST", '127.0.0.1'),
        'PORT': os.environ.get("DB_PORT", '5432'),
    }
}
{% endif %}

ALLOWED_HOSTS = ["127.0.0.1"]

SECRET_KEY = "TESTSECRETKEY"
DEFAULT_FROM_EMAIL = "contact_test@{{cookiecutter.staging_host}}"
{% if cookiecutter.install_rq %}
CACHES = {
    'default': {
        'BACKEND': '{{cookiecutter.project_slug}}.contrib.fake_redis.FakeRedisCache',
    }
}

for key in RQ_QUEUES:
    RQ_QUEUES[key]['ASYNC'] = False
{% endif %}