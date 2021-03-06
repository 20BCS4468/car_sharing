# Generated by Django 3.1.1 on 2022-04-04 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0014_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='car_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='post',
            name='route',
        ),
        migrations.AddField(
            model_name='post',
            name='time_of_trip',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
