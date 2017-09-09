from __future__ import unicode_literals

from django.contrib import messages
from django.core.mail import send_mail
from django.db.models.functions import Now
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import RedirectView
from django.views.generic.edit import DeleteView, FormView, UpdateView
from django.template.loader import render_to_string

from .forms import NewSubscriberForm
from .viewmixins import SubscriberMixin
from ..events.models import Event


class SubscriberUpdateView(SubscriberMixin, UpdateView):
    fields = ['interests']


class SubscriberConfirmView(SubscriberMixin, RedirectView):
    url = reverse_lazy('subscribe')

    def get_redirect_url(self, *args, **kwargs):
        subscriber = self.get_object()
        subscriber.is_confirmed = True
        subscriber.save()
        messages.success(
            self.request,
            'Your subscription has been confirmed. Thanks for signing up!')
        return super(SubscriberConfirmView, self).get_redirect_url(
            *args, **kwargs)


class NewSubscriptionView(FormView):
    form_class = NewSubscriberForm
    template_name = 'subscriptions/new_subscription.html'
    success_url = '/future/'

    def form_valid(self, form):
        subscriber = form.save()
        send_mail(
            subject='EA Boston: Confirm subscription',
            message=render_to_string('subscriptions/confirmation_email.txt',
                                     {'uuid': subscriber.token.uuid}),
            from_email='webmaster@localhost',
            recipient_list=[subscriber.email])
        messages.success(
            self.request,
            'A confirmation email has been sent to {}. Please click the link '
            'in the email to finish subscribing'.format(
                subscriber.email))
        return redirect('subscribe')

    def get_context_data(self, **kwargs):
        context = super(NewSubscriptionView, self).get_context_data(**kwargs)
        context['futureevents'] = Event.objects.filter(start_time__gte=Now()).order_by('start_time')
        return context


class UnsubscribeView(SubscriberMixin, DeleteView):
    success_url = reverse_lazy('subscribe')

    def get_success_url(self, *args, **kwargs):
        messages.success(self.request, 'You have been unsubscribed from all emails.')
        return super(UnsubscribeView, self).get_success_url(*args, **kwargs)
