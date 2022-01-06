import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adra_project.settings.dev')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Celery('adra_project')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()
