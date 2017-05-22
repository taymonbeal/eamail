from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic.edit import FormView, UpdateView

from .forms import NewSubscriberForm
from .viewmixins import SubscriberMixin


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
