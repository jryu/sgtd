from django.conf.urls import patterns, url

from todo import views

urlpatterns = patterns('',
    url(r'^$', views.TodoListView.as_view(), name='todo_list'),
    url(r'^log/$', views.LogCreateView.as_view(), name='todo_log')
)
