from __future__ import unicode_literals

from django.contrib.admin import site as admin_site

from .models import Subscriber, Token


admin_site.register(Subscriber)
admin_site.register(Token)
