from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from todolist.models import Workout
from . import best_friend
from django.shortcuts import render
from .models import Cafriend, Calink
from . import si

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


def workout_update(request):
    title = request.POST.get('workout')

    content = request.POST.get('content')
    name  = User.objects.get(username = request.user.get_username())
    workout = Workout(
        workout = title,
        content = content,
        owner = name)
    workout.save()
    return HttpResponseRedirect(reverse('todolist:today_workout_list'))


def workout_new(request):
    title = request.POST.get('workout')

    content = request.POST.get('content')
    name = User.objects.get(username=request.user.get_username())
    workout = Workout(
        workout=title,
        content=content,
        owner=name)
    workout.save()
    return HttpResponseRedirect(reverse('todolist:today_workout_list'))


 
def today_issue(request):
    #aa = []
    #a = si.riri('openhack2.csv')
    #for i in a:
    #   aa.append(i)


    #name  = User.objects.get(username = request.user.get_username())

    #for a in aa:
    #    calink = Calink(
    #        owner = name,
    #        link = a
    #        )
    #    calink.save()

    calinks = Calink.objects.all()
    
    return render(request, 'todolist/today.html', {'calinks': calinks})