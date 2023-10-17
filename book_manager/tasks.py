import datetime
from datetime import timedelta

from django.contrib.auth.models import User
from django.db.models import Sum, ExpressionWrapper, F, fields
from django.utils import timezone
from celery import shared_task
from .models import UserProfile, ReadingSession


@shared_task
def calculate_reading_statistics():
    users = User.objects.all()
    for user in users:
        total_reading_time_7_days = ReadingSession.objects.filter(
            user=user,
        ).aggregate(
            total_time=Sum(ExpressionWrapper(F('end_time') - F('start_time'), output_field=fields.DurationField()))
        )
        if total_reading_time_7_days['total_time'] is not None:
            total_time_delta = total_reading_time_7_days['total_time']

            total_seconds = total_time_delta.total_seconds()
            total_hours = total_seconds / 3600
            total_hours_rounded = round(total_hours, 2)
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            if not created:
                user_profile.total_reading_time_7_days = total_hours_rounded

                user_profile.save()


@shared_task
def calculate_reading_statistic_per_months():
    users = User.objects.all()
    for user in users:
        total_reading_time_30_days = ReadingSession.objects.filter(
            user=user,
        ).aggregate(
            total_time=Sum(ExpressionWrapper(F('end_time') - F('start_time'), output_field=fields.DurationField()))
        )
        if total_reading_time_30_days['total_time'] is not None:
            total_time_delta = total_reading_time_30_days['total_time']

            total_seconds = total_time_delta.total_seconds()
            total_hours = total_seconds / 3600
            total_hours_rounded = round(total_hours, 2)
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            if not created:
                user_profile.total_reading_time_30_days = total_hours_rounded

                user_profile.save()
