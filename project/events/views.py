from __future__ import unicode_literals

from django.views.generic.list import ListView

from .models import Event
from django.db.models.functions import Now


class EventListView(ListView):
    model = Event
    queryset = Event.objects.filter(start_time__gte=Now()).order_by('start_time')
