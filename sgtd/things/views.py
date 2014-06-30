from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template import RequestContext, loader
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


class IsActionableView(generic.View):
    def get(self, request):
        try:
            stuff = Thing.objects.order_by('datetime_create')[0]
        except IndexError:
            stuff = None

        template = loader.get_template('is_actionable.html')
        context = RequestContext(request, {
            'stuff': stuff,
        })
        return HttpResponse(template.render(context))


class StuffDeleteView(generic.DeleteView):
    model = Thing
    def get_success_url(self):
        return reverse('is_actionable')
