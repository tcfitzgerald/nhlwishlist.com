from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    #url(r'^profile/$', views.profile, name='account'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
)