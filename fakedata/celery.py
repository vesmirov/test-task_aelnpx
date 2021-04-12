import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakedata.settings')

app = Celery('generate_csv')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
