# Generated by Django 4.2.6 on 2023-10-16 20:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_manager', '0002_readingsession'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='readingsession',
            unique_together={('user', 'book')},
        ),
    ]
