# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-29 06:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0009_auto_20180629_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='workout_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 29, 15, 30, 25, 51584), verbose_name='Workout Date'),
        ),
    ]
