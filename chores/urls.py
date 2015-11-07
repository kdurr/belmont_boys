from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /chores/
    url(r'^$', views.index, name='index'),
    # ex:/chores/roomie
    url(r'^roomie/$', views.roomie, name='roomie'),
    # ex:/chores/chore
    url(r'^chore/$', views.chore, name='chore'),
    # ex: /chores/3
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /chores/5/results/
    url(r'^(?P<event_id>[0-9]+)/results/$', views.results, name='results'),
    # new event form link
    url(r'^event/new/$', views.event_new, name='event_new'),
]
