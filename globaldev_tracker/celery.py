import os
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'globaldev_tracker.settings')

app = Celery('globaldev_tracker', broker='redis://redis:6379/0')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

app.conf.beat_schedule = {
    'calculate_user_statistic': {
        'task': 'book_manager.tasks.calculate_reading_statistics',
        'schedule': crontab(hour='0', minute='0', day_of_week='sun')
    },
    'calculate_reading_statistic_per_months': {
        'task': 'book_manager.tasks.calculate_reading_statistic_per_months',
        'schedule': crontab('0', '0', day_of_month='1')
    }

}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
