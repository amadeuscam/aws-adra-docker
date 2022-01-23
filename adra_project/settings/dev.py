from .base import *  # noqa
import os

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'CONN_MAX_AGE': 3600,
        'NAME':  os.environ.get("DATABASE_NAME"),
        'USER': os.environ.get("MYSQL_USER"),
        'PASSWORD': os.environ.get("MYSQL_PASSWORD"),
        'HOST': os.environ.get("MYSQL_HOST"),
        'PORT': 3306,
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = '/static/'
STATIC_URL = '/static/'
