from django.conf.urls.defaults import *
from skatemaps.maps.views import *
import os.path
# Uncomment the next two lines to enable the admin:
from django.contrib import *
admin.autodiscover()

site_media = os.path.join( os.path.dirname(__file__), 'media' )

urlpatterns = patterns('',
    # Example:
    # (r'^skatemaps/', include('skatemaps.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
	(r'^$', index),
	(r'^spots/page/(\d+)/$', spots),
	(r'^spots/(\d+)/$', spotdetail),
	(r'^spots/(\d+)/map/$', spotmap),
	(r'^login/$', 'django.contrib.auth.views.login'),
	#Site media
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media }),
	(r'^logout/$', logout_page),
)
