from django.conf.urls import patterns, url

from todo import views

urlpatterns = patterns('',
    url(r'^$', views.TodoListView.as_view(), name='todo_list'),
    url(r'^check/$', views.LogCreateView.as_view(), name='todo_check'),
    url(r'^uncheck/$', views.LogDeleteView.as_view(), name='todo_uncheck'),
)
