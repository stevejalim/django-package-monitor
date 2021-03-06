# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from django.contrib import admin, staticfiles

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^package_monitor/', include('package_monitor.urls', namespace='package_monitor')),  # noqa
    url(r'^static/(?P<path>.*)$', staticfiles.views.serve),
)
