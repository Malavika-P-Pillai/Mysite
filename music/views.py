# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from music.models import Album,Song


class AlbumListView(ListView):
    model = Album


"""class SongListView(ListView):
    model = Song """


class AlbumCreateView(CreateView):
    model = Album
    fields = ['name','img','genre']
    success_url = '/music/'

class AlbumDetailView(DetailView):
    model = Album
    def get_context_data(self, **kwargs):
        context = super(AlbumDetailView, self).get_context_data(**kwargs)

        song = Song.objects.filter(album=context['album'])
        context['songs'] = song
        return context

    def post(self,request,*args, **kwargs):
        name = request.POST['name']
        artist = request.POST['artist']
        album = Album.objects.get(id=self.kwargs['pk'])

        song = Song(name=name, artist=artist, album=album)
        song.save()

        return redirect('album_detail',album.pk)


class SongDetailView(DetailView):
    model = Song


class AlbumDeleteView(DeleteView):
    model = Album

class SongDeleteView(DeleteView):
    model = Song

"""class SongCreateView(CreateView):
    model = Song
    fields = ['name','artist',]
    success_url = '/music/' """

class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['name', 'img', 'genre']

class SongUpdateView(UpdateView):
    model = Song
    fields = ['name', 'artist']

    def get_success_url(self):
        return reverse('album_detail', kwargs={'pk': self.get_object().album.id})


