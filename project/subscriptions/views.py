from __future__ import unicode_literals

from django.views.generic.edit import UpdateView

from .viewmixins import SubscriberMixin


class SubscriberUpdateView(SubscriberMixin, UpdateView):
    fields = ['interests']
