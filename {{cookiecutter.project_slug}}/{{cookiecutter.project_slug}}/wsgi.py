# -*- coding: utf-8 -*-
import os

try:
    import newrelic.agent as nr
except ImportError:
    pass
else:
    nr.initialize()
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.project_slug}}.settings")
application = get_wsgi_application()
