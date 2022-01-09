from .base import *  # noqa
import os

DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
NAME_DB = os.getenv("DATABASE_NAME")
USER_DB = os.getenv("MYSQL_USER")
PASSWORD_DB = os.getenv("MYSQL_PASSWORD")
HOST = os.getenv("MYSQL_HOST")


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': NAME_DB,
        'USER': USER_DB,
        'PASSWORD': PASSWORD_DB,
        'HOST': HOST,
        'PORT': 3306,
    }
}

EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = str(os.getenv("SENDGRID_API_KEY"))
SENDGRID_ALIMENTOS_TEMPLATE_ID = str(os.getenv("SENDGRID_TEMPLATE_ID"))
SENDGRID_SANDBOX_MODE_IN_DEBUG = False


# aws settings
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
# AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# s3 static settings
AWS_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
