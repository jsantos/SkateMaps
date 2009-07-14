from django.conf.urls.defaults import *
from skatemaps.maps.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^skatemaps/', include('skatemaps.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
	(r'^$', index),
	(r'^spots/$', spots),
	(r'^spots/(\d+)/$', spotdetail),
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/Users/jorgesantos/Documents/workspace/skatemaps/media'}
	),
)
