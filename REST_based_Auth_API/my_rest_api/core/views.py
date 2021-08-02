from decimal import Context
import json

from django.db.models.expressions import OrderBy
from django.http import request
from django.shortcuts import render

from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.fields import NullBooleanField
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Comment, Post, Request
from .serializers import (
    CommentSerializer,
    FriendsSerializer,
    UserSerializer,
    PostSerializer,
    RequestSerializer,
    ChangeRequestStatusSerializer,
    MyTokenObtainPairSerializer,
)
from .utilities import create_notification


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "Hello Faraz!"}
        return Response(content)


class RegisterUserView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(self.serializer_class(user).data)


class GetUsersView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()

    def get_queryset(self):
        return self.queryset.filter(post=self.request.data["post"])


# class RequestView(viewsets.ModelViewSet):
#     serializer_class = RequestSerializer
#     permission_classes = (IsAuthenticated,)
#     queryset = Request.objects.all()

#     def get_queryset(self):
#         return self.queryset.filter(
#             requestee_id=int(self.request.data["requestor"]), status="P"
#         )  # or 'R')


class RequestView(generics.GenericAPIView):
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Request.objects.all()

    # def get_queryset(self):
    #     return self.queryset.filter(
    #         requestee_id=int(self.request.data["requestor"]), status="P"
    #     )  # or 'R')
    def get(self, request, *args, **kwargs):
        return self.queryset.filter(
            requestee_id=int(self.request.data["requestor"]), status="P"
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        # create_notification(
        #     self.request.data["requestee"],
        # )
        user = serializer.save()
        return Response(self.serializer_class(user).data)


class ChangeStatusView(generics.GenericAPIView):
    serializer_class = ChangeRequestStatusSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Request.objects.all()

    def put(self, request, *args, **kwargs):
        user_signed_in = request.user.id
        request = Request.objects.get(pk=request.data["id"])

        if (
            self.request.data["status"] != "P"
            and request.requestee_id == user_signed_in
        ):
            data = self.queryset.filter(pk=self.request.data["id"]).update(
                status=self.request.data["status"]
            )
            # Request.objects.filter(pk=self.request.data['id']).delete()
            data = self.serializer_class(
                Request.objects.get(pk=self.request.data["id"])
            )
            return Response(data.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ShowFriendsView(viewsets.ModelViewSet):
    serializer_class = FriendsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Request.objects.filter(status="A")

    def get_queryset(self):  # (self, request, *args, **kwargs):
        friend_list = []
        user_signed_in_id = self.request.user.id
        user_signed_in = self.request.user
        friends_info = self.queryset.filter(
            requestee=user_signed_in_id
        ) | self.queryset.filter(requestor=user_signed_in_id)
        for friendship in friends_info:
            friend = {}
            if friendship.requestee_id == user_signed_in_id:
                friend["user"] = user_signed_in
                friend["friend"] = friendship.requestor
                friend["status"] = "friends"
            elif friendship.requestor_id == user_signed_in_id:
                friend["user"] = user_signed_in
                friend["friend"] = friendship.requestee
                friend["status"] = "friends"
            friend_list.append(friend)
        return friend_list
