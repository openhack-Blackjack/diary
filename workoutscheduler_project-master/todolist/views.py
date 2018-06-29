from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from todolist.models import Workout


class WorkoutTAV(TodayArchiveView):
    model = Workout
    date_field = 'workout_date'
    allow_empty = True  # Display the page if no objects are available

    # only lists own by logged in user
    def get_queryset(self):
        return Workout.objects.filter(owner_id=self.request.user.id)


class WorkoutDAV(DayArchiveView):
    model = Workout
    date_field = 'workout_date'
    allow_empty = True

    def get_queryset(self):
        return Workout.objects.filter(owner_id=self.request.user.id)


def workout_update(request, workout_id):
    print(workout_id)
    workout = get_object_or_404(Workout, pk=workout_id)  # get workout object from it's primary key
    workout.workout_done = 1
    workout.save()
    return HttpResponseRedirect(reverse('todolist:today_workout_list'))
