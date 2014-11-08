from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(
        r'^users/$',
        views.UserView.as_view({'post': 'create', 'get': 'list'}),
        name='users'),
    url(
        r'^posts/$',
        views.PostView.as_view({'post': 'create', 'get': 'list'}),
        name='posts'
    ),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    #url(r'^users/login/$', include('core.urls', namespace='apiv1')),
)
