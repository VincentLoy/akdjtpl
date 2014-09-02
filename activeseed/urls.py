# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# ActiveSeed Website
# (c) 2014 ActivKonnect

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),
)
