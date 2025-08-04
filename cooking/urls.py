from django.urls import path
from .views import user_login, user_logout, user_register, Index, PostsByCategory, PostDetail, AddPost, PostUpdate

app_name = "cooking"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("category/<int:pk>/", PostsByCategory.as_view(), name="category_list"),
    path("post/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", PostUpdate.as_view(), name="post_update"),
    path("add_post/", AddPost.as_view(), name="add_post"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", user_register, name="register"),
]
