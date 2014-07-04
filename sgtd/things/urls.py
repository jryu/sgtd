from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from things import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="main_page.html"),
        name='main'),
    url(r'^stuff/$', views.StuffListView.as_view(), name='stuff_list'),
    url(r'^stuff/is-actionable/$', views.IsActionableView.as_view(), name='is_actionable'),
    url(r'^stuff/(?P<pk>\d+)/first-action/$', views.FirstActionView.as_view(), name='first_action'),
    url(r'^stuff/(?P<pk>\d+)/delete/$', views.StuffDeleteView.as_view(), name='stuff_delete'),
    url(r'^stuff/(?P<pk>\d+)/maybe/$', views.StuffToMaybeView.as_view(), name='stuff_to_maybe'),
    url(r'^action/$', views.NextActionView.as_view(), name='next_action'),
    url(r'^maybe/$', views.MaybeListView.as_view(), name='maybe_list'),
)
