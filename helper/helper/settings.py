# coding: utf-8
"""
Django settings for helper project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from decouple import config, Csv
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Ex:
# Local == /home/fabiano/projetos/helper/helper
# Prod  == /var/www/projetos/helper/helper

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ADMINS = (
    ('Admin Control H', 'falmeidamelo@uol.com.br'),
)

# Para fazer algum teste que precise de DEBUG = False, ALLOWED_HOSTS não pode ser vazio
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

DEFAULT_FROM_EMAIL = u'contato@controlh.online'


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'test_without_migrations',
    'bootstrap3',
    'localbr',
    'municipios',
    'helper.core',
    'helper.agenda',
    'helper.contabil',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'helper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'helper.wsgi.application'

AUTH_USER_MODEL = 'core.User'

######### CUSTOM LOGIN URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = '/login/'
# See: https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = '/'
# ######### END CUSTOM LOGIN URL CONFIGURATION
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

#  ######### DATABASE CONFIGURATION
DATABASE_ENGINE = config('DATABASE_ENGINE', default='')
DATABASE_NAME = config('DATABASE_NAME', default='')
DATABASE_USER = config('DATABASE_USER', default='')
DATABASE_PASS = config('DATABASE_PASS', default='')
DATABASE_HOST = config('DATABASE_HOST', default='localhost')
DATABASE_PORT = config('DATABASE_PORT', default='5432')

DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASS,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}
#  ######### END DATABASE CONFIGURATION

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# DEFAULT_FILE_STORAGE = config('DEFAULT_FILE_STORAGE')  # media file
# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
# STATICFILES_STORAGE = config('STATICFILES_STORAGE')  # css, js

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfile')
# Ex:
# Local: /home/fabiano/projetos/helper/helper/staticfile

MEDIA_URL= '/media/'
UPLOAD_PATH = os.path.join(BASE_DIR, 'media')
# Ex:
# Local: /home/fabiano/projetos/helper/helper/media

# SECURITY_SETTINGS
## python manage.py check --deploy
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_HTTPONLY = True

# Email configuration
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')


if DEBUG is False:
    INSTALLED_APPS += ('storages',)
    DEFAULT_FILE_STORAGE = config('DEFAULT_FILE_STORAGE')  # media file
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    STATICFILES_STORAGE = config('STATICFILES_STORAGE')  # css, js
    AWS_S3_CUSTON_DOMAIN = "d12ngo9oha73hw.cloudfront.net"  # CDN
    STATIC_URL = "https://%s/staticfile/"  % AWS_S3_CUSTON_DOMAIN
    MEDIA_URL= "https://%s/media/"  % AWS_S3_CUSTON_DOMAIN
