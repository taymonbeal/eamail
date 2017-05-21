from __future__ import unicode_literals

from uuid import uuid1

from django.db.models import (
    EmailField,
    CASCADE,
    Manager,
    ManyToManyField,
    Model,
    OneToOneField,
    UUIDField,
)
from django.urls import reverse
from django.utils.encoding import force_text, python_2_unicode_compatible

from ..events.models import Interest


def create_token():
    return Token.objects.create()


@python_2_unicode_compatible
class Token(Model):

    uuid = UUIDField(unique=True, default=uuid1)

    def __str__(self):
        return force_text(self.uuid)


class SubscriberManager(Manager):

    def from_uuid(self, uuid):
        try:
            token = Token.objects.select_related('subscriber').get(uuid=uuid)
        except Token.DoesNotExist:
            raise InvalidToken
        try:
            return token.subscriber
        except Subscriber.DoesNotExist:
            raise InactiveToken


@python_2_unicode_compatible
class Subscriber(Model):

    email = EmailField(unique=True)
    token = OneToOneField(Token, on_delete=CASCADE, default=create_token)
    interests = ManyToManyField(Interest)

    objects = SubscriberManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('subscriptions', kwargs={'uuid': self.token.uuid})


class InvalidToken(Exception):
    pass


class InactiveToken(Exception):
    pass
