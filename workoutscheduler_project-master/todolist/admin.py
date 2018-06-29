from django.contrib import admin
from todolist.models import Workout


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('workout', 'workout_date', 'owner', 'duration', 'workout_done')


admin.site.register(Workout, WorkoutAdmin)

