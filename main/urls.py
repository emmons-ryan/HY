from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    #blog url
    url(r'^blog/$', views.blog),
    # blog posts url
    url(r'^blog/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # new blog post url
    url(r'^blog/new/$', views.post_new, name='post_new'),
    # edit blog post url
    url(r'^blog/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    ]
