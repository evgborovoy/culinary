from django.urls import path
from .views import index

app_name = "cooking"

urlpatterns = [
    path("", index, name="index"),
]