"""depthealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^faq/', include('faq.urls', namespace="faq")),
    url(r'^support/', include('support.urls', namespace="support")),
    url(r'^reportviewing/', include('reportviewing.urls', namespace="reportviewing")),
    url(r'^reportinput/', include('reportinput.urls', namespace="reportinput")),
    url(r'^register/', include('register.urls', namespace="register")),
    url(r'^login/', include('login.urls', namespace="login")),
    url(r'^admin/', include(admin.site.urls)),
]
