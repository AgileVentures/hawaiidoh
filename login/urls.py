from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    url(r'^$',views.loginscreen, name='login'),
    url(r'^landingpage',views.landingpage, name='landingpage'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^reset', views.resetpassword, name='reset')
]

urlpatterns += staticfiles_urlpatterns()