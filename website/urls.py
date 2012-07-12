from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('website.views',
    # Examples:
    # url(r'^$', 'volunteer_index.views.home', name='home'),
    # url(r'^volunteer_index/', include('volunteer_index.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^$', 'site_index'),
)
