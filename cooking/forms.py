from django import forms
from .models import Post


class PostAddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "category", "photo")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder": "Add description"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
        }
