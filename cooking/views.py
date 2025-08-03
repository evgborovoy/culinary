from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import F

from .models import Post


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


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    Post.objects.filter(pk=pk).update(watched=F("watched") + 1)
    context = {
        "title": post.title,
        "post": post,
    }
    return render(request, "cooking/post_detail.html", context=context)
