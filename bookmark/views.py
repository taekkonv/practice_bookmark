from django.shortcuts import render
from django.views.generic import DetailView, ListView, DeleteView
from .models import Bookmark

class BookmarkListV(ListView):
    model = Bookmark

class BookmarkDetailV(DetailView):
    model = Bookmark