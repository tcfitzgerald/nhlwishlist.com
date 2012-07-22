from django.conf.urls.defaults import *
from django.conf import settings

import views

urlpatterns = patterns('',

    # Wishes
    url(r'^(?P<wish_id>\d+)/$', views.summary, name='wish_summary'),
    url(r'^submit/$', views.submit_wish, name='submit_wish')

)