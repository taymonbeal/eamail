from __future__ import unicode_literals

from django.views.generic.edit import FormView, UpdateView

from .forms import NewSubscriberForm
from .viewmixins import SubscriberMixin


class SubscriberUpdateView(SubscriberMixin, UpdateView):
    fields = ['interests']


class NewSubscriptionView(FormView):
    form_class = NewSubscriberForm
    template_name = 'subscriptions/new_subscription.html'

    def form_valid(self, form):
        print "You submitted a valid form, but we haven't set up any good success behavior yet. Sorry."
