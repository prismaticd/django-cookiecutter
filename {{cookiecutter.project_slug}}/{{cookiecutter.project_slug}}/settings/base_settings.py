# -*- coding: utf-8 -*-

"""
For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import re
from typing import List

from django.template import base

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

DEBUG = False
ALLOWED_HOSTS = []  #  type: List[str]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'django.contrib.sites',
    'django.contrib.humanize',
{% if cookiecutter.install_allauth == "y" %}
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
{% endif %}
    '{{cookiecutter.project_slug}}.apps.home.apps.HomeConfig',

{%- if cookiecutter.install_allauth == "y" %}
    '{{cookiecutter.project_slug}}.apps.myauth',
    '{{cookiecutter.project_slug}}.apps.profile.apps.ProfileConfig',
{%- endif %}

    'import_export',
{%- if cookiecutter.install_rq == "y" %}

    'django_rq',
    'rq_scheduler',
    'django_redis',
{%- endif %}
{%- if cookiecutter.install_wagtail == "y" %}

    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',

    'modelcluster',
    'taggit',
{%- endif %}
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    '{{cookiecutter.project_slug}}.contrib.request.global_middleware',
{%- if cookiecutter.install_allauth == "y" %}
    '{{cookiecutter.project_slug}}.apps.profile.middleware.ProfileMiddleware',
{%- endif %}
{% if cookiecutter.install_wagtail == "y" %}
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
{% endif %}
]  # List[str]

ROOT_URLCONF = '{{cookiecutter.project_slug}}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['{{cookiecutter.project_slug}}/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',
            ],
        },
    },
]

WSGI_APPLICATION = '{{cookiecutter.project_slug}}.wsgi.application'

{% if cookiecutter.install_allauth == "y" %}
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)
{%- endif %}


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Pacific/Auckland'
USE_I18N = False
USE_L10N = False
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s [%(asctime)s] %(name)s.%(funcName)s:%(lineno)s| %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '{{cookiecutter.project_slug}}': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

SITE_ID = 1

STATIC_ROOT = os.path.join(BASE_DIR, '.static')
GTM_ID = None
SETTINGS_EXPORT = [
    'DEBUG',
    'GTM_ID',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'tmp')
MEDIA_URL = '/media/'
MEDIA_SECRET = 'change_me_in_prod'

# this allows Django template tags to span multiple lines.
# http://zachsnow.com/#!/blog/2016/multiline-template-tags-django/
base.tag_re = re.compile(base.tag_re.pattern, re.DOTALL)

{% if cookiecutter.install_rq == "y" %}
CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get("REDIS_URL", "redis://127.0.0.1:6379/1"),
        'OPTIONS': {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    },
}

RQ_QUEUES = {
    'default': {
        'USE_REDIS_CACHE': 'default',
        'ASYNC': True
     },
}
RQ_SHOW_ADMIN_LINK = True
{% endif %}

STATIC_LOGGING = {
    "env": os.environ.get("DJANGO_SETTINGS_MODULE", "").split(".")[-1]
}
{% if cookiecutter.install_wagtail == "y" %}
WAGTAIL_SITE_NAME = '{{cookiecutter.project_slug}}'
{% endif %}

{% if cookiecutter.install_allauth == "y" %}

# DJANGO ALLAUTH CONFIG: http://django-allauth.readthedocs.io/en/stable/configuration.html
ACCOUNT_USER_DISPLAY = "allauth.account.utils.user_email"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_ADAPTER = "{{cookiecutter.project_slug}}.apps.myauth.adapters.AccountAdapter"

LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'profile:edit'
LOGOUT_REDIRECT_URL = 'account_login'
{% endif %}
