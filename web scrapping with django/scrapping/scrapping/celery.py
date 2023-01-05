import os
from time import timezone
from celery import Celery
#from __future__ import absolute_import,unicode_literals
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','scrapping.settings')

app = Celery('scrapping')

app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')
#app.config_from_object(settings, namespace='CELERY')
app.config_from_object('django.conf:settings', namespace='CELERY')

#celery beat settings
app.conf.beat_schedule = {
    
}


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')