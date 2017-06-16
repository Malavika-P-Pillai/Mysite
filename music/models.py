# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='album_img/')
    genre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

class Song(models.Model):
    album = models.ForeignKey(Album)
    name = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)