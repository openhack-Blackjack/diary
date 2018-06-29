from django.conf.urls import url
from todolist.views import *

urlpatterns = [
    # Example: /
    url(r'^$', WorkoutTAV.as_view(), name='default_workout_list'),

    # Example: /today
    url(r'^today/$', WorkoutTAV.as_view(), name='today_workout_list'),

    # Example: /2017/may/25
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', WorkoutDAV.as_view(), name='workout_day_archive'),

    # Example: /workout/update/1
    url(r'^workout/update/$', workout_update, name='workout_update'),

    url(r'^workout/new', workout_new, name='workout_new'),
]
