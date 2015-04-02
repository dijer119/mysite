from django.conf.urls import patterns, url
from lifelog import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^food$', views.food_log_index, name='food_log_index'),
        url(r'^intro$', views.intro, name='intro'),
        url(r'^regist_form$', views.regist_form, name='regist_form'),
        url(r'^regist', views.regist, name='regist'),
        # url(r'^about/$', views.about, name='about'),
        )  # New!