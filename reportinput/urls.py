from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    url(r'epi12a',views.epi12a, name='epi12a'),
    url(r'epi12b',views.epi12b, name='epi12b'),
    url(r'landing12a', views.landing12a, name='landing12a'),
    url(r'landing12b', views.landing12b, name='landing12b'),
    url(r'complete', views.complete, name='complete'),
    url(r'^(?P<student_id>[0-9]+)/update12a', views.update12a, name='update12a'),
    url(r'^(?P<student_id>[0-9]+)/update12b', views.update12b, name='update12b')
]