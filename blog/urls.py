from django.conf.urls import url
from django.contrib import admin

from blog import views
from blog.views import PostListView, PostDetailView

urlpatterns = [

    url(r'^post/$', PostListView.as_view(), name='Home'),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name="view_post"),
    url(r'^add/$', views.add_post, name="add_post"),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.edit_post, name="edit_post"),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.del_post, name="del_post"),
    url(r'^post/del/(?P<pk>[0-9]+)(?P<cn>[0-9]+)$', views.del_comment, name="del_com"),
    url(r'^post/edit/(?P<pk>[0-9]+)/(?P<cn>[0-9]+)$', views.edit_comment, name="edit_com"),


]