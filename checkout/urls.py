__author__ = 'gabriele'

from django.conf.urls import patterns, url
from checkout import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='home'),
        url(r'^about/$', views.about, name='about'),
        # ex: /polls/5/
        url(r'^list/(?P<list_id>\d+)/$', views.display, name='display'),
        # ex: /polls/5/results/
        # url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
        # ex: /list/5/display/
        # url(r'^(?P<list_id>\d+)/display/$', views.display, name='display'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),

        )