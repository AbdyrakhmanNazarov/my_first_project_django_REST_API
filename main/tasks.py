from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def sync_data_from_db(self):
    for i in range(1, 11):
        logger.info(f"[sync_data_from_db] Счёт: {i}")

