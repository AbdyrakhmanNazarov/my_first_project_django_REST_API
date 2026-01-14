from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sync-data-every-hour': {
        'task': 'main.tasks.sync_data_from_db',
        'schedule': crontab(minute=1),
    }
}


# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from celery.schedules import crontab

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
# app = Celery('core')

# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'sync-data-from-1c-every-hour': {
#         'task' : 'apps.main.tasks.sync_data_from_cycle',
#         'schedule': crontab(minute=1),
#     }
# }