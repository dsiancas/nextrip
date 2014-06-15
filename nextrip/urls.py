from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'static/(?P<path>,*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
	(r'media/(?P<path>,*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
	# url(r'^$', 'location.views.location', name='location'),
	# url(r'^$', 'location.views.detail', name='detail'),
	# url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # Examples:
    # url(r'^$', 'nextrip.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'location.views.home', name='home'),
    url(r'^location/', include('location.urls', namespace="location")),
    url(r'^admin/', include(admin.site.urls)),
)