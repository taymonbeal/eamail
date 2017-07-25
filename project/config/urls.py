from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.admin import site as admin_site

from ..events.views import EventDetailView, PastEventListView
from ..subscriptions.views import (
    NewSubscriptionView,
    SubscriberConfirmView,
    SubscriberUpdateView,
    UnsubscribeView,
)


uuid_pattern = (r'(?P<uuid>' +
                r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-' +
                r'[0-9a-f]{12})')


urlpatterns = [
    url(r'^event/(?P<pk>\d+)/$', EventDetailView.as_view(), name='event_detail'),
    url(r'^past/$', PastEventListView.as_view(), name='event_past'),
    url(r'^admin/', admin_site.urls),
    url(r'^$', NewSubscriptionView.as_view(), name='subscribe'),
    url(r'^confirm/{uuid_pattern}/$'.format(uuid_pattern=uuid_pattern),
        SubscriberConfirmView.as_view(),
        name='confirm'),
    url(r'^subscriptions/{uuid_pattern}/$'.format(uuid_pattern=uuid_pattern),
        SubscriberUpdateView.as_view(),
        name='subscriptions'),
    url(r'^unsubscribe/{uuid_pattern}/$'.format(uuid_pattern=uuid_pattern),
        UnsubscribeView.as_view(),
        name='unsubscribe'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin_site.site_header = 'EA Boston Mailing List Control Panel'
admin_site.site_title = 'EA Boston'
admin_site.index_title = 'Mailing List Control Panel'
