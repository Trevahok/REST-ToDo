# Generated by Django 2.0.7 on 2018-12-01 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20181201_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 1, 16, 33, 56, 6381)),
        ),
    ]
