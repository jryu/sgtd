from django.conf.urls import patterns, url

from todo import views

urlpatterns = patterns('',
    url(r'^$', views.TodoListView.as_view(), name='todo_list'),
    url(r'^check/$', views.LogCreateView.as_view(), name='todo_check'),
    url(r'^uncheck/$', views.LogDeleteView.as_view(), name='todo_uncheck'),
    url(r'^log/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$',
        views.TodoDayArchiveView.as_view(month_format='%m'), name='archive_day')
)
