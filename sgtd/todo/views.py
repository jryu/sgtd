from django.core.urlresolvers import reverse
from django.db.models import Max
from django.http import JsonResponse
from django.views import generic
from django.views.generic.base import View
from django.views.generic.dates import DayArchiveView
from django.views.generic.edit import CreateView

from .models import Log, Todo
from .forms import LogForm


class TodoListView(generic.ListView):
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


class LogDeleteView(View):
    def post(self, request, *args, **kwargs):
        form = LogForm(request.POST)
        if form.is_valid():
            Log.objects.filter(todo_id=form.cleaned_data['todo'],
                    date__gte=form.cleaned_data['date']).delete()

            last_date = (Log.objects.filter(todo_id=form.cleaned_data['todo'])
                    .aggregate(Max('date'))['date__max'])

            response = {
              'last_date': last_date,
            }
            if last_date:
                response['year'] = last_date.year
                response['month'] = last_date.month
                response['day'] = last_date.day

            return JsonResponse(response)


class TodoDayArchiveView(DayArchiveView):
    queryset = Log.objects.none()
    date_field = 'date'
    allow_empty = True
    allow_future = True

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DayArchiveView, self).get_context_data(**kwargs)

        context['checked_list'] = (Todo.objects.filter(
            log__date__year=self.get_year(),
            log__date__month=self.get_month(),
            log__date__day=self.get_day())
            .order_by('log__date').distinct())

        context['unchecked_list'] = (Todo.objects.exclude(
            log__date__year=self.get_year(),
            log__date__month=self.get_month(),
            log__date__day=self.get_day()))

        return context
