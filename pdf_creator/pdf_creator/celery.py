import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pdf_creator.settings')

app = Celery('pdf_creator')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
