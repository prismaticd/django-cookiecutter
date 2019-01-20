# -*- coding: utf-8 -*-

from .base_settings import *  # noqa
import os

DEBUG = bool(int(os.environ.get("DEBUG", 0)))
{%- if cookiecutter.database_type == "mysql" %}
DATABASE_VENDOR = os.environ.get("DATABASE_VENDOR", "mysql")
{%- elif cookiecutter.database_type == "postgres" %}
DATABASE_VENDOR = os.environ.get("DATABASE_VENDOR", "postgresql")
{%- endif %}
USE_DEBUG_TOOLBAR = False

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

{% if cookiecutter.database_type == "mysql" %}
if DATABASE_VENDOR == "mysql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.environ.get("MYSQL_DATABASE", "{{cookiecutter.project_slug}}"),
            "USER": os.environ.get("DB_USER", "root"),
            "PASSWORD": os.environ.get("MYSQL_ROOT_PASSWORD"),
            "HOST": os.environ.get("DB_HOST", "127.0.0.1"),
            "PORT": os.environ.get("DB_PORT", "3306"),
            "OPTIONS": {
                "charset": "utf8mb4",
                "init_command": "SET sql_mode='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'",
            },
            "TEST": {"CHARSET": "utf8mb4", "COLLATION": "utf8mb4_unicode_ci"},
        }
    }
{% elif cookiecutter.database_type == "postgres" %}
if DATABASE_VENDOR == "postgresql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB", "postgres"),
            "USER": os.environ.get("POSTGRES_USER", "postgres"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
            "HOST": os.environ.get("DB_HOST", "127.0.0.1"),
            "PORT": os.environ.get("DB_PORT", "5432"),
        }
    }
{% endif %}
elif DATABASE_VENDOR == "sqlite":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
else:
    raise NotImplementedError(f"DATABASE_VENDOR={DATABASE_VENDOR}")


INSTALLED_APPS += [
{%- if cookiecutter.install_behave_test == "y" %}
    "behave_django",
{%- endif %}
]

ALLOWED_HOSTS = ["127.0.0.1"]

SECRET_KEY = "TESTSECRETKEY"
DEFAULT_FROM_EMAIL = "contact_test@{{cookiecutter.staging_host}}"
{% if cookiecutter.install_rq == "y" %}
CACHES = {
    "default": {
        "BACKEND": "{{cookiecutter.project_slug}}.contrib.fake_redis.FakeRedisCache",
    }
}

for key in RQ_QUEUES:
    RQ_QUEUES[key]["ASYNC"] = False
{% endif %}
