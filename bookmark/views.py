from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Bookmark

class BookmarkListV(LoginRequiredMixin, ListView):
    model = Bookmark

class BookmarkDetailV(LoginRequiredMixin, DetailView):
    model = Bookmark

class BookmarkCreateV(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid:
            form.instance.save()
            return redirect('/bookmark/')
        else:
            return self.render_to_response({'form':form})

class BookmarkUpdateV(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteV(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')