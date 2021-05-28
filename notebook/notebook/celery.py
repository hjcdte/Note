import os
from celery import Celery, platforms

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notebook.settings')

platforms.C_FORCE_ROOT = True
app = Celery('notebook')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()