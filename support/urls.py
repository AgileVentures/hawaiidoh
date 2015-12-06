from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    url(r'createticket', views.createrequest, name='create'),
    url(r'openticket', views.viewrequests, name='open'),
    url(r'^r(?P<r_id>[0-9]+)/updateticket', views.updatesupport, name='update'),
    url(r'^r(?P<r_id>[0-9]+)/closeticket', views.closesupport, name='close')
]