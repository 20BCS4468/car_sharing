# Generated by Django 3.1.1 on 2022-03-22 05:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_post_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_of_trip',
            field=models.CharField(default=django.utils.timezone.now, max_length=240),
            preserve_default=False,
        ),
    ]
