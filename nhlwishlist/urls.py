from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'nhlwishlist.apps.wishlist.views.index', name='home'),
    (r'^wishes/', include('nhlwishlist.apps.wishlist.urls')),
    url(r'^tags/(?P<name>[-\w]+)/$', 'nhlwishlist.apps.wishlist.views.tags', name='wish-tag'),
    url(r'^mailinglist/subscribe', 'nhlwishlist.apps.mailinglist.views.subscribe', name='subscribe'),
    (r'^account/', include('nhlwishlist.apps.account.urls')),
    # url(r'^nhlwishlist/', include('nhlwishlist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
