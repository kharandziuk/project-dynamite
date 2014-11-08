from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(
        r'^users/$',
        views.UserView.as_view({'post': 'create', 'get': 'list'}),
        name='users'),
    url(r'^login/$', 'rest_framework_jwt.views.obtain_jwt_token', name='login'),
    url(
        r'^attractions/$',
        views.AttractionView.as_view({'post': 'create', 'get': 'list'}),
        name='attractions'),
    url(
        r'^choice_options/$',
        views.ChoiceView.as_view({'post': 'create', 'get': 'list'}),
        name='choice_options'),
    # url(r'^choice_options/(?P<chooser_id>\w{1,50})/$', view='views.choices_page', name='choice_by_chooser')
    #url(r'^users/login/$', include('core.urls', namespace='apiv1')),
)