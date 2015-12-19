from django.conf.urls import patterns, url

from todo import views

urlpatterns = patterns('',
    url(r'^$', views.MainView.as_view(), name='todo_main'),
    url(r'^check/$', views.LogCreateView.as_view(), name='todo_check'),
    url(r'^uncheck/$', views.LogDeleteView.as_view(), name='todo_uncheck'),
    url(r'^log/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$',
        views.TodoDayArchiveView.as_view(month_format='%m'), name='todo_archive'),
    url(r'^edit/$', views.TodoListView.as_view(), name='todo_edit_list'),
    url(r'^create/$', views.TodoCreateView.as_view(), name='todo_create'),
    url(r'^update/(?P<pk>\d+)$', views.TodoUpdateView.as_view(), name='todo_update'),
    url(r'^delete/(?P<pk>\d+)$', views.TodoDeleteView.as_view(), name='todo_delete'),
    url(r'^trend/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$',
        views.TodoTrendView.as_view(month_format='%m'), name='todo_trend'),
)
