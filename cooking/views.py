from django.http import HttpRequest
from django.shortcuts import render

from .models import Category, Post

def index(request: HttpRequest):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "cooking/index.html", context=context)
