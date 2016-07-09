__author__ = 'emmanuel'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^monitor/json/load/serverdata', views.loadData, name='loadData'),
]