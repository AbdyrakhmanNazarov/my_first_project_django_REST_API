from celery import shared_task
from django.db import transaction
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 3, 'countdown': 10})
def sync_data_from_db(self):
    with transaction.atomic():
        for i in range(10):
            logger.info(f"Счёт: {i}")
