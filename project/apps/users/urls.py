from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^users/$', views.UserView.as_view({'post': 'create'}), name='users'),
    #url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    #url(r'^users/login/$', include('core.urls', namespace='apiv1')),
)
