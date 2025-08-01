from .models import Category, Post
from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", "title"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "created_at", "category"]
