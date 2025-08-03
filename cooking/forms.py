from django import forms
from .models import Post
from django.contrib.auth.forms import AuthenticationForm


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


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username",
                               max_length=127,
                               widget=forms.TextInput(attrs={"class": "form-control"}),
                               )
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(attrs={"class": "form-control"}),
                               )
