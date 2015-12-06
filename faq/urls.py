from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    url(r'^category/',views.category, name='category'),
    url(r'^(?P<category_id>[0-9]+)/questions', views.faq, name='questions')
]
