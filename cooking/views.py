from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from django.contrib.auth import login, logout

from .models import Post
from .forms import PostAddForm, LoginForm


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
    post_recommends = Post.objects.exclude(pk=pk).order_by("-watched")[:5]
    context = {
        "title": post.title,
        "post": post,
        "post_recommends": post_recommends,
    }
    return render(request, "cooking/post_detail.html", context=context)


def add_post(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            post.save()
            return redirect("cooking:post_detail", post.pk)
    else:
        form = PostAddForm()

    context = {
        "title": "Add post",
        "form": form,
    }
    return render(request, "cooking/add_post.html", context=context)


def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print("for is valid")
            user = form.get_user()
            login(request, user)  # without authenticate because it has inside form
            return redirect("cooking:index")
    else:
        form = LoginForm()
    context = {
        "title": "Login",
        "form": form,
    }
    return render(request, "cooking/login_form.html", context=context)


def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("cooking:index")
