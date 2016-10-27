from __future__ import unicode_literals

from django.contrib.admin import site as admin_site

from .models import Event, Interest


admin_site.register(Event)
admin_site.register(Interest)
