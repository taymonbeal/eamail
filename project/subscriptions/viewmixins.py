from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.detail import SingleObjectMixin

from .models import InactiveToken, InvalidToken, Subscriber


class SubscriberMixin(SingleObjectMixin):

    model = Subscriber

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(SubscriberMixin, self).dispatch(
                request, *args, **kwargs)
        except InvalidToken:
            return render(
                request, 'subscriptions/invalid_token.html', status=403)
        except InactiveToken:
            return render(
                request, 'subscriptions/inactive_token.html', status=404)

    def get_object(self):
        return Subscriber.objects.from_uuid(self.kwargs['uuid'])
