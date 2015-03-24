from django.conf.urls import patterns, url
from lifelog import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^intro$', views.intro, name='intro'),
        # url(r'^about/$', views.about, name='about'),
        )  # New!