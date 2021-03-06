from django.conf.urls import url
from django.views.generic import TemplateView

from things import views
from things.models import Thing

urlpatterns = [
    url(r'^$',
        TemplateView.as_view(template_name='main_page.html'), name='main'),

    url(r'^stuff/$', views.StuffListView.as_view(), name='stuff_list'),

    # This is different from 'thing_delete'. The default value of 'success_url'
    # for STUFF is 'is_stuff_actionable', but deleting from 'stuff_list' should
    # return back to 'stuff_list' itself.
    url(r'^stuff/(?P<pk>\d+)/delete/$',
        views.ThingDeleteView.as_view(success_url='stuff_list'),
        name='stuff_delete'),

    # Asks if a STUFF is actionable and then asks what is its first action
    # item.
    url(r'^stuff/is-actionable/$',
        views.IsStuffActionableView.as_view(), name='is_stuff_actionable'),
    url(r'^stuff/(?P<pk>\d+)/first-action/$',
        views.FirstActionView.as_view(), name='first_action'),

    # List views
    url(r'^action/$',
        views.ThingListView.as_view(
            category=Thing.ACTION, template_name='action_list.html'),
        name='action_list'),
    url(r'^waiting/$',
        views.ThingListView.as_view(
            category=Thing.WAITING, template_name='waiting_list.html'),
        name='waiting_list'),
    url(r'^maybe/$',
        views.ThingListView.as_view(
            category=Thing.MAYBE, template_name='maybe_list.html'),
        name='maybe_list'),

    # Main page of a Thing
    url(r'^thing/(?P<pk>\d+)/is-actionable/$',
        views.IsSingleObjectActionableView.as_view(),
        name='is_thing_actionable'),

    # Update category
    url(r'^thing/(?P<pk>\d+)/to-waiting/$',
        views.CategoryUpdateView.as_view(new_category=Thing.WAITING),
        name='to_waiting'),
    url(r'^thing/(?P<pk>\d+)/to-maybe/$',
        views.CategoryUpdateView.as_view(new_category=Thing.MAYBE),
        name='to_maybe'),

    # Update Thing.text
    url(r'^thing/(?P<pk>\d+)/text_update/$',
        views.TextUpdateView.as_view(), name='text_update'),

    # Delete
    url(r'^thing/(?P<pk>\d+)/delete/$', views.ThingDeleteView.as_view(),
        name='thing_delete'),
]
