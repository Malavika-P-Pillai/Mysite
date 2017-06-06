from django.conf.urls import url
from django.contrib import admin

from blog import views
from blog.views import PostListView, PostDetailView

urlpatterns = [

    url(r'^post/$', PostListView.as_view(), name='Home'),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name="view_post"),

]