from django.shortcuts import render
from django.http import HttpResponse

posts = [
        {
            'author':'author1',
            'title':'title1',
            'content':'content1',
            'date_posted': 'date1'
        },
        {
            'author':'another1',
            'title':'title2',
            'content':'content2',
            'date_posted': 'somedate'
        }
    ]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})