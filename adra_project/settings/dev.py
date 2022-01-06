from .base import *  # noqa
import os

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Database
NAME_DB = os.environ.get("DATABASE_NAME")
USER_DB = os.environ.get("MYSQL_USER")
PASSWORD_DB = os.environ.get("MYSQL_PASSWORD")
HOST = os.environ.get("MYSQL_HOST")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'CONN_MAX_AGE': 3600,
        'NAME': NAME_DB,
        'USER': USER_DB,
        'PASSWORD': PASSWORD_DB,
        'HOST': HOST,
        'PORT': 3306,
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = '/static/'
STATIC_URL = '/static/'
