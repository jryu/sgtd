from django.db.models import Max
from django.views import generic

from todo.models import Todo


class TodoListView(generic.ListView):
    template_name = 'todo_list.html'

    def get_queryset(self):
        return (Todo.objects.annotate(last_date=Max('log__date'))
                .order_by('last_date'))
