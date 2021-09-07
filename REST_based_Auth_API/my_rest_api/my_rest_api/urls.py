"""my_rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from core import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", views.HelloView.as_view(), name="hello"),
    path("register/", views.RegisterUserView.as_view(), name="register"),
    path(
        "post/", views.PostView.as_view({"post": "create", "get": "list"}), name="post"
    ),
    path(
        "home/", views.HomeView.as_view({"get": "list"}), name="home"
    ),
    path(
        "comment/",
        views.CommentView.as_view({"post": "create", "get": "list"}),
        name="comment",
    ),
    path(
        "like/",
        views.LikeView.as_view({"post": "create", "get": "list"}),
        name="like",
    ),
    path("get_users/",
         views.GetUsersView.as_view({"get": "list"}), name="get_users"),
    path(
        "request/",
        views.RequestView.as_view({"post": "create", "get": "list"}),
        name="request",
    ),
    path(
        "message/",
        views.MessageView.as_view({"post": "create", "get": "list"}),
        name="message",
    ),
    path(
        "change_status/",
        views.ChangeStatusView.as_view({"put": "update", "delete": "destroy"}),
        name="change_status",
    ),
    path(
        "friends/",
        views.FriendsView.as_view({"get": "list", "delete": "destroy"}),
        name="friends",
    ),
    path(
        "show_notifications/",
        views.ShowNotifications.as_view({"get": "list", "put": "update"}),
        name="show_notifications",
    ),
    
    path(
        "api/token/", views.MyTokenObtainPairView.as_view(), name="my_token_obtain_pair"
    ),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
    # path(
    #     "api/token/verify/", views.MyTokenVerifyView.as_view(), name="token_verify"
    # ),
]
