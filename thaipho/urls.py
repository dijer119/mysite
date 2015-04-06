from django.conf.urls import patterns, url
from thaipho import views

urlpatterns = patterns('',
        url(r'^$', views.index2, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^contact/$', views.contact, name='contact'),
        url(r'^menu/$', views.menu, name='menu'),
        # url(r'^about/$', views.about, name='about'),
        )  # New!