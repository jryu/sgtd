from django.core.urlresolvers import reverse
from django.views import generic

from things.models import Thing

class StuffListView(generic.CreateView):
    template_name = 'stuff_list.html'
    model = Thing

    def get_context_data(self, **kwargs):
        context = super(StuffListView, self).get_context_data(**kwargs)
        context['object_list'] =  Thing.objects.order_by('-datetime_create')
        return context

    def get_success_url(self):
        return reverse('stuff_list')
