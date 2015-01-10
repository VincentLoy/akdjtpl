# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# {{ project_name }}
# (c) 2014 ActivKonnect

from os import getenv

import dj_database_url

from .utils import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

SITE_ID = 1

INSTALLED_APPS = (
    # Base Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Helper apps
    'djangobower',
    'pipeline',

    # Our apps
    '{{ project_name }}.apps.accounts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(),
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATIC_ROOT = DJANGO_ROOT.child('assets')

STATICFILES_DIRS = (
    DJANGO_ROOT.child('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'pipeline.finders.PipelineFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# Templates

TEMPLATE_DIRS = (
    DJANGO_ROOT.child('templates'),
)

# Get SECRET_KEY from env
SECRET_KEY = getenv('SECRET_KEY')

# Email sending
DEFAULT_FROM_EMAIL = 'EMAIL-SENDER@EXAMPLE.COM'

# Analytics
METRON_SETTINGS = {
    "google": {
        1: getenv('GOOGLE_ANALYTICS_UID', ''),
    }
}

# Other common config files

from .bower import *
from .pipeline import *
