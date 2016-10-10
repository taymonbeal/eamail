from __future__ import unicode_literals

from django.db.models import (
    CharField,
    DateTimeField,
    ImageField,
    Model,
    TextField,
)
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Event(Model):

    title = CharField(max_length=150)
    description = TextField()
    location = CharField(max_length=254)
    start_time = DateTimeField()
    end_time = DateTimeField(null=True, blank=True)
    picture = ImageField()

    def __str__(self):
        return self.title
