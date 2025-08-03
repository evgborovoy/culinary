from django.urls import path
from .views import index, category_list, post_detail, add_post, user_login, user_logout

app_name = "cooking"

urlpatterns = [
    path("", index, name="index"),
    path("category/<int:pk>/", category_list, name="category_list"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("add_post/", add_post, name="add_post"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
]
