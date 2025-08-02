from .models import Category, Post
from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    list_display_links = ("pk", "title")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "created_at", "category", "is_published")
    list_display_links = ("pk", "title")
