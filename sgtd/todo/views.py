from datetime import date

from django.db.models import Max
from django.shortcuts import render
from django.views import generic


from todo.models import Todo

class TodoListView(generic.ListView):
    template_name = 'todo_list.html'

    def get_queryset(self):
        return (Todo.objects.annotate(last_time=Max('log__datetime_create'))
                .order_by('last_time'))

    def get_context_data(self, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)
        context['today'] = date.today()
        return context
