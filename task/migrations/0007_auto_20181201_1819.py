# Generated by Django 2.0.7 on 2018-12-01 18:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20181201_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 1, 18, 19, 57, 635702, tzinfo=utc)),
        ),
    ]
