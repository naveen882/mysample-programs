from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('registration.views',
    url(r'^reg/$', 'reg_index'),
    url(r'^send/$', 'send'),
    url(r'^login/$', 'log_in'),
    url(r'^logon/$', 'logon'),
    url(r'^list/$', 'list'),
    url(r'^update/$', 'update'),
    url(r'^delete/$', 'delete'),
    url(r'^get_user/$', 'get_user'),
)
