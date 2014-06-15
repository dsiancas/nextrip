from django.conf.urls import patterns, url

from location import views

urlpatterns = patterns('',
    # ex: /polls/
    # url(r'^$', views.home, name='home'),
    url(r'^(?P<detail_id>\d+)/$', views.detail, name='detail'),
    #url(r'^detail/$', views.detail, name='detail'),
    # ex: /polls/5/
    url(r'^detail/$', views.get_cart, name='get_cart'),
    
    url(r'^detail/$', views.add_cart, name='add_cart'),
    
    # ex: /polls/5/results/
    # url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    # url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    # added the word 'specifics'
	# url(r'^specifics/(?P<poll_id>\d+)/$', views.detail, name='detail'),
)