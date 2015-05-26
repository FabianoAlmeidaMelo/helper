# coding: utf-8

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'helper',
        'USER': 'thom',
        'PASSWORD': 'thom',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
