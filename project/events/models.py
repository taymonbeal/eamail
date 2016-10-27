from __future__ import unicode_literals

from django.db.models import (
    CharField,
    DateTimeField,
    ImageField,
    ManyToManyField,
    Model,
    PositiveSmallIntegerField,
    TextField,
)
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Interest(Model):

    name = CharField(max_length=150, unique=True)
    order = PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Event(Model):

    name = CharField(max_length=150)
    location = CharField(max_length=254)
    start_time = DateTimeField()
    end_time = DateTimeField(null=True, blank=True)
    description = TextField()
    picture = ImageField()
    interests = ManyToManyField(Interest)

    def __str__(self):
        return self.name
