# Generated by Django 4.2.6 on 2023-10-16 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_manager', '0004_alter_readingsession_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readingsession',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='readingsession',
            unique_together={('user', 'book')},
        ),
    ]
