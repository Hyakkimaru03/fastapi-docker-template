import os

from celery import Celery

REDIS_URL = os.getenv("REDIS_URL")
celery_app = Celery('worker', broker=REDIS_URL, backend=REDIS_URL, include=[])

celery_app.conf.beat_schedule = {}

# celery_app.conf.timezone = "Asia/Dubai"
celery_app.conf.enable_utc = True

if __name__ == "__main__":
    celery_app.start()
