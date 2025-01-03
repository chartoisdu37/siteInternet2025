from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  #A voir l utilisation de CreateView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostUpdateView(UpdateView):
    model = Post
    fields = (
        "title",
        "body",
    )
    template_name = "post-edit.html"

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post_list")

class PostCreateView(CreateView):
    model = Post
    template_name = "home.html"
    fields = (
        "title",
        "author",
        "body",
    )



