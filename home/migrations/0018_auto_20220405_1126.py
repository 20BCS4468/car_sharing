# Generated by Django 3.1.1 on 2022-04-05 05:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20220405_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_of_trip',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_of_trip',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]