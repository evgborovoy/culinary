from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import *

app_name = "cooking"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("category/<int:pk>/", PostsByCategory.as_view(), name="category_list"),
    path("post/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", PostUpdate.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDelete.as_view(), name="post_delete"),
    path("add_post/", AddPost.as_view(), name="add_post"),
    path("search/", SearchResults.as_view(), name="search"),
    path("change_password/", UserChangePassword.as_view(), name="change_password"),

    path("post/<int:pk>/add_comment/", add_comment, name="add_comment"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", user_register, name="register"),
    path("profile/<int:user_id>/", profile, name="profile"),

    # API
    path("api/posts/", PostListAPI.as_view(), name="posts_list_api"),
    path("api/posts/<int:pk>/", PostDetailAPI.as_view(), name="posts_detail_api"),
    path("api/categories/", CategoryListAPI.as_view(), name="category_list_api"),
    path("api/categories/<int:pk>/", CategoryDetailAPI.as_view(), name="category_detail_api"),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
