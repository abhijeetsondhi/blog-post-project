# Generated by Django 2.0.2 on 2018-05-08 03:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_auto_20180507_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 8, 3, 5, 38, 741375, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 8, 3, 5, 38, 741375, tzinfo=utc)),
        ),
    ]
