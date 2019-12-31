from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import (  ListView, 
                                    DetailView,
                                    CreateView,
                                    )
from django.contrib.auth.mixins import LoginRequiredMixin

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

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content'] #<app>/<model>_form.html

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title':'about'})