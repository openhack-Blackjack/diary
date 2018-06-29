from django.views.generic.base import TemplateView

from django.utils.safestring import mark_safe

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, mpld3
import numpy as np


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