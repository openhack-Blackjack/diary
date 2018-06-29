# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-29 06:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_auto_20180629_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='content',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 29, 15, 4, 46, 298572), verbose_name='Workout Date'),
        ),
    ]