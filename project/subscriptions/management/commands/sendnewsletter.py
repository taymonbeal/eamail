from __future__ import unicode_literals

from datetime import timedelta

from django.core.mail import get_connection, send_mail
from django.core.management.base import BaseCommand
from django.db.models.functions import Now, TruncDate
from django.template.loader import render_to_string

from ...models import Subscriber
from ....events.models import Event, Interest


class Command(BaseCommand):

    help = 'Sends out newsletters to all subscribers'

    def handle(self, *args, **options):
        with get_connection() as connection:
            for subscriber in Subscriber.objects.all():
                events = Event.objects.filter(
                    interests__subscriber=subscriber,
                    start_time__date__gte=TruncDate(Now()),
                    start_time__date__lt=(TruncDate(Now()) + timedelta(days=7)),
                ).distinct().order_by('start_time', 'name')
                if events:
                    send_mail(
                        subject='EA Boston Weekly Newsletter',
                        message=render_to_string(
                            'subscriptions/newsletter.txt', {'events': events}),
                        from_email='webmaster@localhost',
                        recipient_list=[subscriber.email],
                        connection=connection)
