from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    url(r'^userlist', views.userfilter,name='userlist'),
    url(r'^(?P<person_id>[0-9]+)/modifyuser',views.modifyuser, name='modifyuser'),
    url(r'^(?P<facility_id>[0-9]+)/modify',views.modifyfacility, name='modify'),
    url(r'list', views.facilitylist, name='facilitylist'),
    url(r'facilityinput',views.facility, name='facilityinput'),
    url(r'createuser', views.createuser,name='createuser'),
    url(r'user', views.username,name='user'),
    url(r'^(?P<facility_id>[0-9]+)/facilitylanding', views.facilitylanding,name='facilitylanding')
]