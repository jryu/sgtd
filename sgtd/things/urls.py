from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from things import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="main_page.html"),
        name='main'),
    url(r'^stuff/$', views.StuffListView.as_view(), name='stuff_list'),
)
