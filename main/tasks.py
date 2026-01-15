from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task(
    bind=True,
    name='apps.main.tasks.sync_data_from_db'
)
def sync_data_from_db(self):
    """
    Простая задача: выводит числа от 1 до 10
    """
    for i in range(1, 11):
        logger.info(f"[sync_data_from_db] Счёт: {i}")
