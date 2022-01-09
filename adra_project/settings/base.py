import os
from sentry_sdk.integrations.django import DjangoIntegration
import sentry_sdk

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# django-allauth config
SITE_ID = 1
SESSION_COOKIE_AGE = 86400

TOKEN_KEY_USER = os.environ.get("Token_KEY_USER")
# Application definition


INSTALLED_APPS = [
    # local
    'adra.apps.AdraConfig',
    # default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_filters',
    'crispy_forms',
    # auth zone
    'allauth',
    'allauth.account',
    # api zone rest
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    # s3 amazon
    'storages'



]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware'
]

ROOT_URLCONF = 'adra_project.urls'

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
                'adra.context_processors.add_variable_to_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'adra_project.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,

    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.\
            UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.\
            MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.\
            CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.\
            NumericPasswordValidator',
    },
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",

]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-eu'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = 'adra:persona-home'
ACCOUNT_LOGOUT_REDIRECT = 'adra:persona-home'  # new

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )


DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_EMAIL")
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400  # 1 day in seconds
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_SIGNUP_FORM_CLASS = 'adra.forms.SignupForm'
ACCOUNT_ADAPTER = 'adra.views.CustomAllauthAdapter'

# chache page
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'cache_table',
    }
}

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 600  # una semana
CACHE_MIDDLEWARE_KEY_PREFIX = ''

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# CORS_ORIGIN_ALLOW_ALL =

CORS_ALLOWED_ORIGINS = [
    # "http://localhost:8080",
    "http://127.0.0.1:8080",
    'https://adra-django-static.s3.amazonaws.com'
]
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)


sentry_sdk.init(
    dsn=f"{os.environ.get('SENTRY_SDK_URL')}",
    integrations=[DjangoIntegration()]
)


CELERY_BROKER_URL = str(os.environ.get("REDIS_URL"))
CELERY_RESULT_BACKEND = str(os.environ.get("REDIS_URL"))
CELERY_USER = str(os.environ.get("CELERY_USER"))
CELERY_USER_PASSWORD = str(os.environ.get("CELERY_PASSWORD"))
TELEGRAM_TOKEN_KEY = str(os.environ.get("TELEGRAM_TOKEN"))


PLATFORM_NAME = "Adra Torrejon"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        '': {
            'level': 'DEBUG',
            # 'handlers': ['console', 'file'],
            'handlers': ['console'],
            'propagate': True,
        }
    },
    'formatters': {
        'console': {
            'format': '%(asctime)s  %(name)-12s %(levelname)-8s %(message)s'
        },
        # 'file': {
        #     'format': '%(asctime)s  %(name)-12s %(levelname)-8s %(message)s'
        # }

    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        # 'file': {
        #     'level': 'DEBUG',
        #     'class': 'logging.FileHandler',
        #     'filename': os.path.join(BASE_DIR, 'adra_logs/debug.log'),
        #     # 'maxBytes': '16777216',  # 16megabytes
        #     'formatter': 'file'
        # }
    },

}

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
