from django.views.generic.base import TemplateView

from django.utils.safestring import mark_safe

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, mpld3
import numpy as np

from todolist.models import Workout, WorkoutList


class StatsTV(TemplateView):
    template_name = 'workoutstats.html'

    def get_context_data(self, **kwargs):
        context = super(StatsTV, self).get_context_data(**kwargs)

        my_workouts = Workout.objects.filter(
            owner_id=self.request.user.id, workout_done=1  # 소유자와 일치하고 이미 한 운동만 쿼리
        )

        # 카테고리와 시간을 튜플로 생성 (category, duration)하여 리스트에 삽입
        graph_raw_data = []
        for workout in my_workouts:
            graph_raw_data.append((WorkoutList.objects.get(id=workout.workout_id).category_id, workout.duration))

        # 카테고리별로 합쳐서 Data 가공
        # 카테고리가 1, 2, 3, 4, 5이므로 1씩 빼준다

        data_list = [0] * 5

        for data in graph_raw_data:
            data_list[data[0]-1] += data[1]

        piechart = plot_piechart(self.request, data_list)
        context['piechart'] = mark_safe(piechart)


        # 꺾은선 그래프
        graph = plot_graph(self.request)
        context['graph'] = mark_safe(graph)

        # 바 그래프
        barchart = plot_barchart(self.request)
        context['barchart'] = mark_safe(barchart)
        return context


def plot_graph(request):
    fig = plt.figure(figsize=(5, 5))
    plt.plot([1, 2, 3, 4])
    return mpld3.fig_to_html(fig)


# Plot chiepart in template Usage : {{ piechart }}
# counter clockwise from 12'o clock
# Label, size args로 넘기면 그려주도록

def plot_piechart(request, sizes):
    labels = ['스트렝스', '파워', '근지구력', '지구력', '기타']
    explode = (0.05, 0.05, 0.05, 0.05, 0.05)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots(figsize=(5, 5))
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    return mpld3.fig_to_html(fig1)


def plot_barchart(request):
    n_groups = 5
    means_men = (20, 35, 30, 35, 27)
    std_men = (2, 3, 4, 1, 2)

    means_women = (25, 32, 34, 20, 25)
    std_women = (3, 5, 2, 3, 3)

    fig, ax = plt.subplots(figsize=(5, 5))

    index = np.arange(n_groups)
    bar_width = 0.35

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(index, means_men, bar_width,
                     alpha=opacity,
                     color='b',
                     yerr=std_men,
                     error_kw=error_config,
                     label='Men')

    rects2 = plt.bar(index + bar_width, means_women, bar_width,
                     alpha=opacity,
                     color='r',
                     yerr=std_women,
                     error_kw=error_config,
                     label='Women')

    plt.xlabel('종류')
    plt.ylabel('Scores')
    #plt.title('Scores by group and gender')
    plt.xticks(index + bar_width / 2, ('A', 'B', 'C', 'D', 'E'))
    plt.legend()

    plt.tight_layout()

    return mpld3.fig_to_html(fig)

# https://matplotlib.org/examples/api/radar_chart.html // Personal characteristic Graph