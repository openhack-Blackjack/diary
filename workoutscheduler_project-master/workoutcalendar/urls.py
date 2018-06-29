from django.conf.urls import url
from workoutcalendar.views import *

urlpatterns = [
    # Example: /
    url(r'^$', WorkoutCalendarTV.as_view(), name='workout_calendar'),

    # Example: /2017/5/
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', WorkoutCalendarTV.as_view(), name='workout_month_calendar'),
]