from django.core.urlresolvers import reverse
from django import http
from django.template import RequestContext, loader
from django.views import generic

from things.models import Thing
from things.forms import TextUpdateForm


def get_default_url_name_for_category(category):
    return {
        Thing.STUFF: 'is_stuff_actionable',
        Thing.ACTION: 'next_action',
        Thing.MAYBE: 'maybe_list',
    }[category]

class StuffListView(generic.CreateView):
    template_name = 'stuff_list.html'
    model = Thing
    fields = ['text']

    def get_context_data(self, **kwargs):
        context = super(StuffListView, self).get_context_data(**kwargs)
        context['object_list'] =  Thing.objects.filter(
                category=Thing.STUFF).order_by('-datetime_create')
        return context

    def form_valid(self, form):
        form.instance.category = Thing.STUFF
        return super(generic.CreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('stuff_list')


class IsActionableView(generic.View):
    def get(self, request, *args, **kwargs):
        stuff = self.get_object()
        template = loader.get_template('is_actionable.html')
        context = RequestContext(request, {
            'stuff': stuff,
            'category_stuff': Thing.STUFF,
            'category_action': Thing.ACTION,
            'category_maybe': Thing.MAYBE,
        })
        return http.HttpResponse(template.render(context))


class IsStuffActionableView(IsActionableView):
    def get_object(self):
        try:
            return Thing.objects.filter(category=Thing.STUFF).order_by(
                    'datetime_create')[0]
        except IndexError:
            return None


class IsSingleObjectActionableView(generic.detail.SingleObjectMixin, IsActionableView):
    model = Thing


class ThingDeleteView(generic.DeleteView):
    model = Thing
    success_url = None

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        if self.success_url is None:
            return reverse(get_default_url_name_for_category(
                self.object.category))
        else:
            return reverse(self.success_url)


class CategoryUpdateView(generic.detail.SingleObjectMixin, generic.View):
    model = Thing
    new_category = None

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        thing = self.get_object()
        prev_category = thing.category
        thing.category = self.new_category
        thing.save()
        return http.HttpResponseRedirect(reverse(
            get_default_url_name_for_category(prev_category)))


class NextActionView(generic.ListView):
    template_name = 'next_action.html'

    def get_queryset(self):
        return Thing.objects.filter(
                category=Thing.ACTION).order_by('-datetime_update')


class MaybeListView(generic.ListView):
    template_name = 'maybe_list.html'

    def get_queryset(self):
        return Thing.objects.filter(
                category=Thing.MAYBE).order_by('-datetime_create')


class FirstActionView(generic.UpdateView):
    model = Thing
    fields = ['text']
    template_name = 'first_action.html'
    prev_category = None

    def form_valid(self, form):
        self.prev_category = self.object.category
        form.instance.category = Thing.ACTION
        return super(generic.UpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse(get_default_url_name_for_category(self.prev_category))


class TextUpdateView(generic.UpdateView):
    model = Thing
    fields = ['text']
    template_name = 'text_update.html'
    form_class = TextUpdateForm

    def get_success_url(self):
        return reverse(get_default_url_name_for_category(self.object.category))
