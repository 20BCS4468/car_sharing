# Generated by Django 3.1.1 on 2022-03-28 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20220329_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='car_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='post',
            name='destination',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='post',
            name='participants',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='post',
            name='route',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='post',
            name='source',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='post',
            name='vacant_seats',
            field=models.CharField(max_length=120),
        ),
    ]
