from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def homepage_view(request):
    print(request.user)
    map = {
        "title": "Home Page - Blog",
        "posts": Post.objects.all()
    }
    return render(request,"blog/homePage_Blog.html",map)


def aboutPage_view(request):
    print(request.user)
    map = {
        "title": "About - Blog",
        "content": "yooooo"
    }
    return render(request,"blog/about_Blog.html",map)