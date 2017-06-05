# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import ImageField


"""def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)"""


class Post(models.Model):
    title = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_published = models.BooleanField(default=False)
    description = models.TextField(default="content")
    img = ImageField(upload_to='blog_img/')
    user = user = models.ForeignKey(User)
    def __unicode__(self):
        return self.title


class Comment(models.Model):
    comment_text = models.TextField(default="content")
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    date =  models.DateTimeField(auto_now=True, auto_now_add=False)
    def __unicode__(self):
        return self.comment_text