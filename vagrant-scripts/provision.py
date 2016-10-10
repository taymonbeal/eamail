from __future__ import unicode_literals

from django import setup
setup()

from django.contrib.auth.models import User
from django.contrib.sites.models import Site


User.objects.create_superuser(username='admin', email=None, password='admin')
Site.objects.update(domain='localhost:8000', name='EA Boston Newsletter')
