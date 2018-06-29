# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-29 05:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20170608_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutlist',
            name='category',
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workout',
            name='workout_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 29, 14, 36, 53, 982492), verbose_name='Workout Date'),
        ),
        migrations.DeleteModel(
            name='WorkoutCategory',
        ),
        migrations.DeleteModel(
            name='WorkoutList',
        ),
    ]
