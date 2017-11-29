# -*- coding: utf-8 -*-

from .base_settings import *

{% if cookiecutter.database_type == "mysql" %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("MYSQL_DATABASE"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("MYSQL_ROOT_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),
    }
}
{% elif cookiecutter.database_type == "postgres" %}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DB"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),
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