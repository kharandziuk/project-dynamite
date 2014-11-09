from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(
        r'^attractions/$',
        views.AttractionView.as_view({'post': 'create', 'get': 'list'}),
        name='attractions'),
    # url(r'^choice_options/(?P<chooser_id>\w{1,50})/$', view='views.choices_page', name='choice_by_chooser')
    #url(r'^users/login/$', include('core.urls', namespace='apiv1')),
)