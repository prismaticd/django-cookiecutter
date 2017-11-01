# -*- coding: utf-8 -*-

from .base_settings import *


DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Django debug toolbar
# To disable add those 2 lines in local.py:
# INSTALLED_APPS.remove('debug_toolbar')
# MIDDLEWARE.remove('debug_toolbar.middleware.DebugToolbarMiddleware')
INSTALLED_APPS += ['debug_toolbar', 'django_extensions',]
MIDDLEWARE[:0] = ['debug_toolbar.middleware.DebugToolbarMiddleware',]

INTERNAL_IPS = ['127.0.0.1', 'localhost']
{% if cookiecutter.install_rq == "y" %}
CACHES = {
    'default': {
        'BACKEND': '{{cookiecutter.project_slug}}.contrib.fake_redis.FakeRedisCache',
    }
}

for key in RQ_QUEUES:
    RQ_QUEUES[key]['ASYNC'] = False
{% endif %}


try:
    from .local import *
except ImportError:  # pragma: no cover
    import random
    raise Exception("settings/local.py file is missing, create one with the line SECRET_KEY = '{}'".format(
        ''.join((random.choice("abcdefghijklmnopqrstuvwxyz")) for x in range(48))))
