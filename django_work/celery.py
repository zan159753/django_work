
# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_work.settings')

app = Celery('django_work')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'rotate-passwords': {
#         'task': 'hosts.tasks.rotate_host_passwords',
#         # 'schedule': crontab(minute=0, hour='*/8'),
#         'schedule': 5.0,
#     },
#     'daily-stats': {
#         'task': 'hosts.tasks.generate_daily_stats',
#         'schedule': crontab(minute=52, hour=10),
#     },
# }