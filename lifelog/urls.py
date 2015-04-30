from django.conf.urls import patterns, url
from lifelog import views

urlpatterns = patterns('',
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^food$', views.food_log_index, name='food_log_index'),
        url(r'^intro$', views.intro, name='intro'),
        url(r'^(?P<log_id>[0-9]+)/modify_form$', views.ModifyFormView.as_view(), name='modify_form'),
        url(r'^(?P<log_id>[0-9]+)/modify$', views.modify, name='modify'),
        url(r'^regist_form$', views.regist_form, name='regist_form'),
        url(r'^regist_form2$', views.regist_form2, name='regist_form2'),
        url(r'^regist$', views.regist, name='regist'),
        url(r'^regist2$', views.regist2, name='regist2'),
        # url(r'^about/$', views.about, name='about'),
        )  # New!