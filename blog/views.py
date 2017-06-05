# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import generic as generic
from django.shortcuts import render

# Create your views here.
from blog.models import Post, Comment

"""class Home(generic.ListView):
    model = Post
    template_name = '/blog/home.html' """

def home(request):
    posts = Post.objects.all()
    template = 'blog/home.html'

    for i in posts:
        i.description = i.description[0:100] + "......"

    context = {"posts": posts}
    return render(request, template, context)

def view_post(request,id):
    post = Post.objects.get(id=int(id))
    comment = Comment.objects.filter(post=post)
    template = 'blog/view.html'
    context = {"post": post,"comments":comment}
    return render(request, template, context)