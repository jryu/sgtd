from django.core.urlresolvers import reverse
from django.db.models import Max
from django.http import JsonResponse
from django.views import generic
from django.views.generic.edit import CreateView

from todo.models import Log, Todo


class TodoListView(generic.ListView):
    template_name = 'todo_list.html'

    def get_queryset(self):
        return (Todo.objects.annotate(last_date=Max('log__date'))
                .order_by('last_date'))


# https://docs.djangoproject.com/en/1.9/topics/class-based-views/generic-editing/#ajax-example
class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class LogCreateView(AjaxableResponseMixin, CreateView):
    model = Log
    template_name = 'log_form.html'

    def get_success_url(self):
        return reverse('todo_list')
