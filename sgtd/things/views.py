from django.core.urlresolvers import reverse
from django import http
from django.template import RequestContext, loader
from django.views import generic

from things.models import Thing

class StuffListView(generic.CreateView):
    template_name = 'stuff_list.html'
    model = Thing

    def get_context_data(self, **kwargs):
        context = super(StuffListView, self).get_context_data(**kwargs)
        context['object_list'] =  Thing.objects.filter(
                category=Thing.STUFF).order_by('-datetime_create')
        return context

    def get_success_url(self):
        return reverse('stuff_list')


class IsActionableView(generic.View):
    def get(self, request):
        try:
            stuff = Thing.objects.filter(category=Thing.STUFF).order_by(
                    'datetime_create')[0]
        except IndexError:
            stuff = None

        template = loader.get_template('is_actionable.html')
        context = RequestContext(request, {
            'stuff': stuff,
        })
        return http.HttpResponse(template.render(context))


class StuffDeleteView(generic.DeleteView):
    model = Thing

    def get_success_url(self):
        return reverse('is_actionable')


class StuffToMaybeView(generic.detail.SingleObjectMixin, generic.View):
    model = Thing

    def post(self, request, *args, **kwargs):
        thing = self.get_object()
        thing.category = Thing.MAYBE
        thing.save()
        return http.HttpResponseRedirect(reverse('is_actionable'))


class MaybeListView(generic.ListView):
    template_name = 'maybe_list.html'

    def get_queryset(self):
        return Thing.objects.filter(
                category=Thing.MAYBE).order_by('-datetime_create')
