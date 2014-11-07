from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api-v1/', include('users.urls', namespace='api-v1')),
)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
