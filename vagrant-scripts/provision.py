from __future__ import unicode_literals

from django import setup
setup()

from django.contrib.auth.models import User
from django.contrib.sites.models import Site


Site.objects.update(domain='localhost:8000', name='EA Boston Newsletter')
User.objects.create_superuser(username='admin', password='admin', email=None)
