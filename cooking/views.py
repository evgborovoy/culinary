from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Category, Post


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    context = {
        "title": "Recipes",
        "posts": posts,
    }
    return render(request, "cooking/index.html", context=context)


def category_list(request: HttpRequest, pk: int) -> HttpResponse:
    posts = Post.objects.filter(category_id=pk)
    context = {
        "title": posts[0].category,
        "posts": posts,
    }
    return render(request, "cooking/index.html", context=context)
