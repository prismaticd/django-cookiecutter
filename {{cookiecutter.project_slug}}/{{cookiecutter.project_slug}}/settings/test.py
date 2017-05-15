# -*- coding: utf-8 -*-

from .base_settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("MYSQL_DATABASE"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("MYSQL_ROOT_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT "),
    }
}

ALLOWED_HOSTS = ["127.0.0.1"]

SECRET_KEY = "TESTSECRETKEY"
DEFAULT_FROM_EMAIL = "contact_test@{{cookiecutter.staging_host}}"

CACHES = {
    'default': {
        'BACKEND': '{{cookiecutter.project_slug}}.contrib.fake_redis.FakeRedisCache',
    }
}

for key in RQ_QUEUES:
    RQ_QUEUES[key]['ASYNC'] = False
