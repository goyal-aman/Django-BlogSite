from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

#home
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

#post detailed 
class PostDetailView(DetailView):
    model = Post #<app>/<model_name>_<view type>

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})