from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Устанавливаем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Создаём приложение Celery
app = Celery('core')

# Загружаем настройки из Django с префиксом CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим tasks.py в приложениях
app.autodiscover_tasks()

# ========================
# Настройка Beat
# ========================

app.conf.beat_schedule = {
    # Пример: задача sync_data_from_cycle каждые 1 час
    'sync-data-from-1c-every-hour': {
        'task': 'apps.main.tasks.sync_data_from_cycle',  # путь к функции в tasks.py
        'schedule': crontab(minute='*/3'),  # каждый 3 минут
        'options': {'queue': 'default'},  # очередь Celery (опционально)
    },
}

# ========================
# Общие настройки Celery
# ========================
app.conf.update(
    timezone='Asia/Bishkek',     
    enable_utc=True,
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
)
