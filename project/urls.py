from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
from core import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.TestPageView.as_view(), name='index'),
)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
