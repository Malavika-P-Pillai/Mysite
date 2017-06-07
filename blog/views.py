# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect





from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

from django.shortcuts import render, redirect
from django.template import context
from django.views import generic, View
# Create your views here.
from blog.models import Post, Comment

class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/home.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/view.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)

        comment = Comment.objects.filter(post=context['post'])
        context['comments'] = comment
        return context
    def add_comment(self,request):
        if request.method == "POST":
            post = context['post']
            user = User.objects.get(username=request.user.username)
            comment_text = request.POST['comment_text']
            new_comment = Comment(comment_text=comment_text, user=user)
            new_comment.save()
            return redirect('view_post', post.id)

def signup(request):
    template = 'registration/signup.html'
    context = {}
    if request.method == 'POST':
        firstname = request.POST ['firstname']
        lastname = request.POST ['lastname']
        email = request.POST ['email']
        username = request.POST ['username']
        password1 = request.POST ['password1']
        password2 = request.POST ['password2']

        user = User.objects.filter(email=email)
        if len(user) != 0:
            context['errors'] = "Email is already taken"
            return render(request, template, context)

        user = User.objects.filter(username=username)
        if len(user) != 0:
            context['errors'] = "Username is already taken"
            return render(request, template, context)

        if password1 == password2:
            user = User(first_name=firstname, last_name=lastname, email=email, username=username)
            user.set_password(password1)
            user.save()
            return redirect('login')

    return render(request, template, context)



    """def add_comment(self,request):
        if request.method == "POST":
            comment_text = request.POST['comment']
            user = User.objects.get(username=request.user.username)
            comment = Comment.objects.filter(post=context['post'])
            comment= Comment(comment_text=comment_text, user=user)
            return redirect('view_post', post..id)"""

"""class MyFormView(View):
    form_class = Comment
    initial = {'comment_text': 'value'}
    template_name = 'blog/view.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'comment': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():

            return HttpResponseRedirect('/blog')

        return render(request, self.template_name, {'form': form}"""


def add_post(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        img = request.FILES['img']
        is_published = request.POST['is_published']
        user = User.objects.get(username=request.user.username)
        new_post = Post(title=title, description=description, img=img, is_published=is_published, user=user)
        new_post.save()
        return redirect('view_post',new_post.id)
    else:
        template = 'blog/add_post.html'
        context = {}
        return render(request, template, context)



def edit_post(request,pk):
    post = Post.objects.get(id=int(pk))
    if request.user.username != post.user.username:
        raise PermissionDenied
    if request.method == "GET":
        template = 'blog/post_edit.html'
        context = {'post':post}
        return render(request,template,context)
    else:
        post.title = request.POST['title']
        post.description = request.POST['description']

        if 'img' in request.FILES:
            post.img = request.FILES["img"]
        if 'is_published' in request.POST:
            post.is_published = request.POST['is_published']

        post.save()
        return redirect('view_post', post.id)


def del_post(request,pk):
    post = Post.objects.get(id=int(pk))
    if request.user.username != post.user.username:
        raise PermissionDenied
    if post is not None:
        post.delete()
        return redirect('Home')

def del_comment(request,pk):
    post = Post.objects.get(id=int(pk))
    comment = Comment.objects.filter(post=post)
    if request.user.username != post.user.username:
        raise PermissionDenied
    if comment is not None:
        comment.delete()
        return redirect('Home')


"""
class AddPost(generic.CreateView):
    model=Post
    template_name = "blog/add_post.html"
    fields = [title...]
    success_url = '/blog'
    
class DeletePostView(generic.DeleteView):
    model=Post
    success_url = '/'
"""

"""def home(request):
    posts = Post.objects.all()
    template = 'blog/home.html'

    for i in posts:
        i.description = i.description[0:100] + "......"

    context = {"posts": posts}
    return render(request, template, context)"""

"""def view_post(request,id):
    post = Post.objects.get(id=int(id))
    comment = Comment.objects.filter(post=post)
    template = 'blog/view.html'
    context = {"post": post,"comments":comment}
    return render(request, template, context)"""