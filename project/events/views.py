from __future__ import unicode_literals

from django.views.generic.list import ListView
from django.db.models.functions import Now

from .models import Event


class EventListView(ListView):
    model = Event
    queryset = Event.objects.filter(start_time__gte=Now()).order_by('start_time')


class PastEventListView(ListView):
    model = Event
    queryset = Event.objects.filter(start_time__lte=Now()).order_by('-start_time')
    template_name = 'events/event_list.html'
