from django.conf.urls import url
from workoutstats.views import *

urlpatterns = [
    # Example: /
    url(r'^$', StatsTV.as_view(), name='graph_list'),
]
