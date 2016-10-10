from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.admin import site as admin_site

from events.views import EventListView


urlpatterns = [
    url(r'^$', EventListView.as_view()),
    url(r'^admin/', admin_site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin_site.site_header = 'EA Boston Mailing List Control Panel'
admin_site.site_title = 'EA Boston'
admin_site.index_title = 'Mailing List Control Panel'
