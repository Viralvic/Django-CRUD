from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Post

# Create your views here.

class PostListView(CreateView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ["__all__"]
    success_url = success_url = reverse_lazy("blog:all")

class PostDetailView(CreateView):
    model = Post

class PostUpdateView(CreateView):
    model = Post
    fields = ["__all__"]
    success_url = reverse_lazy("blog:all")

class PostDeleteView(CreateView):
    model = Post
    fields = ["__all__"]
    success_url = reverse_lazy("blog:all")