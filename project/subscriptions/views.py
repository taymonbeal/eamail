from __future__ import unicode_literals

from django.contrib import messages
from django.db.models.functions import Now
from django.shortcuts import redirect
from django.views.generic.edit import FormView, UpdateView

from .forms import NewSubscriberForm
from .viewmixins import SubscriberMixin
from ..events.models import Event


class SubscriberUpdateView(SubscriberMixin, UpdateView):
    fields = ['interests']


class NewSubscriptionView(FormView):
    form_class = NewSubscriberForm
    template_name = 'subscriptions/new_subscription.html'
    success_url = '/future/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you for subscribing.')
        return redirect('event_list')

    def get_context_data(self, **kwargs):
        context = super(NewSubscriptionView, self).get_context_data(**kwargs)
        context['futureevents'] = Event.objects.filter(start_time__gte=Now()).order_by('start_time')
        return context
