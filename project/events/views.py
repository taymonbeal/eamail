from __future__ import unicode_literals

from django.db.models.functions import Now
from django.views.generic import DetailView
from django.views.generic.list import ListView

from .models import Event

class EventDetailView(DetailView):
    model = Event


class PastEventListView(ListView):
    model = Event
    queryset = Event.objects.filter(start_time__lte=Now()).order_by('-start_time')
    template_name = 'events/past_event_list.html'
