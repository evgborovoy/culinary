from django.http import HttpRequest
from django.shortcuts import render

from .models import Category, Post


def index(request: HttpRequest):
    categories = Category.objects.all()
    posts = Post.objects.all()
    context = {
        "posts": posts,
        "categories": categories,
    }
    return render(request, "cooking/index.html", context=context)
