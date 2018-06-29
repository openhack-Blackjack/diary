from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User




@python_2_unicode_compatible
class Workout(models.Model):
    workout = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    # record modified time for object
    # This will be used to figure out when this workout performed (by checking workout_done flag)
    workout_date = models.DateTimeField('Workout Date', default=datetime.today())
    duration = models.IntegerField('Duration', default=0)

    owner = models.ForeignKey(User, null=False)
    workout_done = models.BooleanField(default=False)  # flag to check whether workout done or not

    def __str__(self):
        return str(self.workout)



class Calink(models.Model):
    owner = models.ForeignKey(User, null=False)
    link = models.CharField(max_length= 100)
    create_date = models.DateTimeField(default=datetime.today())