from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from things import views
from things.models import Thing

urlpatterns = patterns('',
    url(r'^$',
        TemplateView.as_view(template_name="main_page.html"), name='main'),

    url(r'^stuff/$', views.StuffListView.as_view(), name='stuff_list'),
    url(r'^stuff/is-actionable/$',
        views.IsStuffActionableView.as_view(), name='is_stuff_actionable'),
    url(r'^stuff/(?P<pk>\d+)/first-action/$',
        views.FirstActionView.as_view(), name='first_action'),
    url(r'^stuff/(?P<pk>\d+)/not-actionable/$',
        views.ThingDeleteView.as_view(success_url='is_stuff_actionable'),
        name='not_actionable'),

    url(r'^action/$', views.NextActionView.as_view(), name='next_action'),
    url(r'^waiting/$', views.WaitingListView.as_view(), name='waiting_list'),
    url(r'^maybe/$', views.MaybeListView.as_view(), name='maybe_list'),

    url(r'^thing/(?P<pk>\d+)/is-actionable/$',
        views.IsSingleObjectActionableView.as_view(),
        name='is_thing_actionable'),
    url(r'^thing/(?P<pk>\d+)/text_update/$',
        views.TextUpdateView.as_view(), name='text_update'),

    # Update category
    url(r'^thing/(?P<pk>\d+)/to-action/$',
        views.CategoryUpdateView.as_view(new_category=Thing.ACTION),
        name='to_action'),
    url(r'^thing/(?P<pk>\d+)/to-waiting/$',
        views.CategoryUpdateView.as_view(new_category=Thing.WAITING),
        name='to_waiting'),
    url(r'^thing/(?P<pk>\d+)/to-maybe/$',
        views.CategoryUpdateView.as_view(new_category=Thing.MAYBE),
        name='to_maybe'),

    # Delete
    url(r'^thing/(?P<pk>\d+)/delete/$', views.ThingDeleteView.as_view(),
        name='thing_delete'),
)
