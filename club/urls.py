# coding:utf-8
__author__ = 'albert'

from django.conf.urls import include, url
from django.contrib import admin
from club.views import index
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
]