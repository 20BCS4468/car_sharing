# Generated by Django 3.1.1 on 2022-03-28 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20220322_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_of_trip',
            field=models.DateTimeField(),
        ),
    ]
