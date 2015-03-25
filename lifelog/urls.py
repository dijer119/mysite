from django.conf.urls import patterns, url
from lifelog import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^food$', views.food_log_index, name='food_log_index'),
        url(r'^intro$', views.intro, name='intro'),
        # url(r'^about/$', views.about, name='about'),
        )  # New!