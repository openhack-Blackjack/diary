from datetime import date, datetime
from calendar import HTMLCalendar, month_name
from itertools import groupby
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape as esc
from django.urls import reverse
from todolist.models import Workout

def pop(request, id):
    workout = Workout.objects.filter(id = id)

    return render(request, 'child.html', {'workouts': workout})

class WorkoutCalendarTV(TemplateView):
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super(WorkoutCalendarTV, self).get_context_data(**kwargs)
        year = datetime.now().year
        month = datetime.now().month

        if 'year' in self.kwargs and 'month' in self.kwargs:
            year = int(self.kwargs['year'])
            month = int(self.kwargs['month'])

        my_workouts = Workout.objects.order_by('workout_date').filter(
            workout_date__year=year, workout_date__month=month, owner_id=self.request.user.id
        )
        cal = WorkoutCalendar(my_workouts).formatmonth(year, month)
        context['calendar'] = mark_safe(cal)
        return context


class WorkoutCalendar(HTMLCalendar):

    def __init__(self, workouts):
        super(WorkoutCalendar, self).__init__(firstweekday=6)  # start from sunday (pass argument to super function)
        self.workouts = self.group_by_day(workouts)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today orange lighten-3'
            if day in self.workouts:
                cssclass += ' filled'
                body = ['<ul>']
                for workout in self.workouts[day]:
                    body.append('<li><h6>')
                    body.append('<a href = /calendar/popcontent/' + str(workout.id) + '>' + esc(workout.workout) + '</a>')
                    body.append("<div style = 'display: none;''>"+"<input type = 'text' name = 'content'>" + esc(workout.content) + "</input>"+"</div>")
                    body.append('</li></h6>')
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonthname(self, year, month, withyear=True):
        if withyear:
            s = '%s %s' % (month_name[month], year)
        else:
            s = '%s' % month_name[month]
        return '<tr><th colspan="1" class="month_arrow">' \
               '<a href="%s"><i class="fa fa-arrow-left" aria-hidden="true"></i></a></th>' \
               '<th colspan="5" class="month">%s</th>' \
               '<th colspan="1" class="month_arrow">' \
               '<a href="%s"><i class="fa fa-arrow-right" aria-hidden="true"></i><a/></th></tr>' \
               % (reverse('calendar:workout_month_calendar', kwargs=self.get_previous_month(year, month)), s,
                  reverse('calendar:workout_month_calendar', kwargs=self.get_next_month(year, month)))

    # return one-month calendar
    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(WorkoutCalendar, self).formatmonth(year, month)

    @classmethod
    def group_by_day(cls, workouts):
        field = lambda workout: workout.workout_date.day
        return dict(
            [(day, list(items)) for day, items in groupby(workouts, field)]
        )

    @classmethod
    def day_cell(cls, cssclasses, body):
        return '<td class="%s">%s</td>' % (cssclasses, body)

    @classmethod
    def get_previous_month(cls, year, month):
        if month == 1:
            return {"year": year-1, "month": 12}
        else:
            return {"year": year, "month": month-1}

    @classmethod
    def get_next_month(cls, year, month):
        if month == 12:
            return {"year": year + 1, "month": 1}
        else:
            return {"year": year, "month": month + 1}


