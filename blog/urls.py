from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^worker/(?P<pk>\d+)/$', views.worker, name='worker'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^cooperation$', views.Cooperation.as_view(), name='cooperation'),
    url(r'^publication/(?P<pk>\d+)/$', views.publication, name='publication'),
    url(r'^worker/(?P<worker_id>\d+)/publications/$', views.publications, name='publications'),
    url(r'^worker/(?P<worker_id>\d+)/pageWithTests/$', views.pageWithTests, name='pageWithTests'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]

#urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    #url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
#]