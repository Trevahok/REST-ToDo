# Generated by Django 2.0.7 on 2018-12-01 16:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20181201_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 1, 16, 47, 17, 886260, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('c37c4e04-f588-11e8-bdb5-14109fdfa251')),
        ),
    ]
