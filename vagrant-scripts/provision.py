from __future__ import unicode_literals

from django import setup
setup()

from django.contrib.sites.models import Site

from project.emailauth.models import User


Site.objects.update(domain='localhost:8000', name='EA Boston Newsletter')
User.objects.create_superuser(email='admin@localhost', password='admin')
