# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-29 05:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_auto_20180629_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='workout_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 29, 14, 50, 49, 962222), verbose_name='Workout Date'),
        ),
    ]
