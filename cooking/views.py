from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from django.contrib.auth import login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Category
from .forms import PostAddForm, LoginForm, RegistrationForm


class Index(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "cooking/index.html"
    extra_context = {"title": "Recipes"}


class PostsByCategory(Index):
    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs["pk"], is_published=True)

    def get_context_data(self, *, object_list=..., **kwargs):
        context = super().get_context_data()
        category = get_object_or_404(Category, pk=self.kwargs["pk"])
        context["title"] = category.title
        return context


class PostDetail(DetailView):
    template_name = "cooking/post_detail.html"

    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        Post.objects.filter(pk=self.kwargs["pk"]).update(watched=F("watched") + 1)
        context = super().get_context_data()
        post = self.object
        context["title"] = post.title
        post_recommends = Post.objects.exclude(pk=self.kwargs["pk"]).order_by("-watched")[:5]
        context["post_recommends"] = post_recommends
        return context


class AddPost(CreateView):
    form_class = PostAddForm
    template_name = "cooking/add_post.html"
    extra_context = {"title": "Add post"}


class PostUpdate(UpdateView):
    model = Post
    form_class = PostAddForm
    template_name = "cooking/add_post.html"


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy("cooking:index")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.is_published = False
        self.object.save()
        return HttpResponseRedirect(success_url)


def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print("for is valid")
            user = form.get_user()
            login(request, user)  # without authenticate because it has inside form
            messages.success(request, "You have successfully logged in")
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


def user_register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("cooking:login")
    else:
        form = RegistrationForm()
    context = {
        "form": form,
        "title": "Register"
    }
    return render(request, "cooking/user_register.html", context=context)
