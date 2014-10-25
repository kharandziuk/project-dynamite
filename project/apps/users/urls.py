from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^users/$', views.UserView.as_view({'post': 'create', 'get': 'list'}), name='users'),
    url(r'^login/$', 'rest_framework_jwt.views.obtain_jwt_token', name='login'),
    #url(r'^users/login/$', include('core.urls', namespace='apiv1')),
)
