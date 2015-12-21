from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from todo import views

urlpatterns = [
    url(r'^$', login_required(views.Main.as_view()), name='todo_main'),
    url(r'^check/$', login_required(
        views.LogCreate.as_view()), name='todo_check'),
    url(r'^uncheck/$', login_required(
        views.LogDelete.as_view()), name='todo_uncheck'),
    url(r'^log/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$',
        login_required(views.TodoDayArchive.as_view(month_format='%m')),
        name='todo_archive'),
    url(r'^edit/$', login_required(
        views.TodoList.as_view()), name='todo_edit_list'),
    url(r'^create/$', login_required(
        views.TodoCreate.as_view()), name='todo_create'),
    url(r'^update/(?P<pk>\d+)$', login_required(
        views.TodoUpdate.as_view()), name='todo_update'),
    url(r'^delete/(?P<pk>\d+)$', login_required(
        views.TodoDelete.as_view()), name='todo_delete'),
    url(r'^trend/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$',
        login_required(views.TodoTrend.as_view(month_format='%m')),
        name='todo_trend'),
]
