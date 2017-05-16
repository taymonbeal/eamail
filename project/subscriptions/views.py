from __future__ import unicode_literals

from django.views.generic.edit import FormView, UpdateView

from .forms import NewSubscriberForm
from .viewmixins import SubscriberMixin


class SubscriberUpdateView(SubscriberMixin, UpdateView):
    fields = ['interests']


class NewSubscriptionView(FormView):
    form_class = NewSubscriberForm
