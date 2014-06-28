from django.views import generic

from things.models import Thing

class StuffListView(generic.ListView):
    template_name = 'stuff_list.html'

    def get_queryset(self):
        return Thing.objects.order_by('-datetime_update')
