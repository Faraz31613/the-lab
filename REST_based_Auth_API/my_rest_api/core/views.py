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

from .models import Comment, Friend, Like, Message, Notification, Post, Request
from .serializers import (
    CommentSerializer,
    FriendsSerializer,
    LikeSerializer,
    NotificationSerializer,
    UserSerializer,
    PostSerializer,
    RequestSerializer,
    MessageSerializer,
    ChangeRequestStatusSerializer,
    MyTokenObtainPairSerializer,
)
from .utilities import create_notification, save_friend


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
        post_id = self.request.data["post"]
        comment_id = self.request.data["comment"]

        if comment_id:  # checking it because it can be null
            return self.queryset.filter(comment=comment_id)
        return self.queryset.filter(post=post_id)

    def create(self, request, *args, **kwargs):
        signed_in_user = self.request.user.id
        post_id = self.request.data["post"]
        comment_id = self.request.data["comment"]

        commentor = User.objects.get(pk=signed_in_user)
        parent_post = Post.objects.get(pk=post_id)
        if not parent_post:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        post_author = parent_post.user_id

        if comment_id:
            parent_comment = Comment.objects.get(pk=comment_id)
            if not parent_comment:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            comment_type = Comment.CommentType.COMMENT
            notification_text = (
                f"{commentor.username} has replied to a Comment on your post"
            )

        else:
            comment_type = Comment.CommentType.POST
            notification_text = f"{commentor.username} has Commented on your post"

        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        create_notification(
            request,
            to_user=User(post_author),
            notification=notification_text,
            notification_source_type=comment_type,
            user_by=signed_in_user,
            notification_source_id=notification_source_id,
        )
        create_notification(
            request,
            to_user=User(post_author),
            notification=notification_text,
            notification_source_type=comment_type,
            user_by=User(signed_in_user),
            post=post_id,
            comment=comment_id,
        )
        comment = serializer.save()
        return Response(self.serializer_class(comment).data)


class RequestView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Request.objects.all()

    def get_queryset(self):
        signed_in_user = self.request.user.id
        return Request.objects.filter(requestee=signed_in_user, status="P")

    def create(self, request, *args, **kwargs):
        signed_in_user_id = self.request.user.id
        signed_in_user = self.request.user
        if signed_in_user_id == self.request.data["requestee"]:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # request_exists_or_not
        if Request.objects.filter(
            requestor_id=signed_in_user_id
        ) | Request.objects.filter(requestee_id=signed_in_user_id):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=self.request.data)

        requestor = User.objects.get(pk=self.request.data["requestor"])

        serializer.is_valid(raise_exception=True)
        create_notification(
            request,
            to_user=User(self.request.data["requestee"]),
            notification=f"{requestor.username} has sent you a Friend Request",
            notification_source_type=Notification.NotificationType.REQUEST,
            user_by=signed_in_user,
            post=None,
            comment=None,
        )
        request = serializer.save()
        return Response(
            self.serializer_class(request).data, status=status.HTTP_201_CREATED
        )


class ChangeStatusView(viewsets.ModelViewSet):
    serializer_class = ChangeRequestStatusSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Request.objects.all()

    def update(self, request, *args, **kwargs):
        signed_in_user_id = self.request.user.id
        signed_in_user = self.request.user
        request_id = request.data["id"]
        request = Request.objects.get(pk=request_id)

        # requestee changes status
        if (
            self.request.data["status"]
            == Request.Status.ACCEPTED  # for rejecting, call delete
            and request.requestee_id == signed_in_user_id
        ):
            self.queryset.filter(pk=request_id).update(
                status=self.request.data["status"]
            )
            acceptor = User.objects.get(pk=signed_in_user_id)
            create_notification(
                request,
                to_user=User(request.requestor_id),
                notification=f"{acceptor.username} has accepted your friend request",
                notification_source_type=Notification.NotificationType.REQUEST,
                user_by=signed_in_user,
                post=None,
                comment=None,
            )
            save_friend(
                request,
                user=User(request.requestor_id),
                friend=User(request.requestee_id),
                friend_request=request,
            )
            save_friend(
                request,
                user=User(request.requestee_id),
                friend=User(request.requestor_id),
                friend_request=request,
            )
            data = self.serializer_class(Request.objects.get(pk=request_id))
            return Response(data.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        signed_in_user = request.user.id
        request_id = request.data["id"]
        request = Request.objects.get(pk=request_id)

        # requestor cancels request or requestee rejects request
        if (
            self.request.data["status"] == Request.Status.REJECTED
            and request.requestor_id == signed_in_user
            or request.requestee_id == signed_in_user
        ):

            # delete notification that was send to requestee
            Notification.objects.filter(
                user=request.requestee_id,
                user_by=request.requestor_id,
                notification_source_type=Notification.NotificationType.REQUEST,
            ).delete()

            # request deletion
            self.queryset.filter(pk=request_id).delete()

            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_401_UNAUTHORIZED)


class FriendsView(viewsets.ModelViewSet):
    serializer_class = FriendsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Friend.objects.all()

    def get_queryset(self):
        signed_in_user = self.request.user
        return self.queryset.filter(user=signed_in_user)

    def destroy(self, request, *args, **kwargs):
        signed_in_user = self.request.user
        friend = self.queryset.get(
            user=signed_in_user, friend=self.request.data["friend"]
        )
        request = friend.request
        request = Request.objects.get(pk=request.id)
        print((request))
        # both were friends, unfriend them and delete request

        self.queryset.filter(
            user=request.requestor_id, friend=request.requestee_id
        ).delete()
        self.queryset.filter(
            user=request.requestee_id, friend=request.requestor_id
        ).delete()
        Request.objects.filter(pk=request.id).delete()
        return Response(status=status.HTTP_200_OK)


class ShowNotifications(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Notification.objects.all()

    def get_queryset(self):
        signed_in_user = self.request.user.id
        return self.queryset.filter(user=signed_in_user)


class LikeView(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Like.objects.all()

    def get_queryset(self):
        post = self.request.data["post"]
        comment = self.request.data["comment"]

        if comment:  # checking it because it can be null
            return self.queryset.filter(comment=comment)
        return self.queryset.filter(post=post)

    def create(self, request, *args, **kwargs):
        signed_in_user = self.request.user.id
        post_id = self.request.data["post"]
        comment_id = self.request.data["comment"]

        user_liked = User.objects.get(pk=signed_in_user)
        parent_post = Post.objects.get(pk=post_id)
        if not parent_post:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        post_author = parent_post.user_id

        if comment_id:
            parent_comment = Comment.objects.get(pk=comment_id)
            if not parent_comment:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            like_type = Like.LikeType.COMMENT
            notification_text = f"{user_liked} has liked your comment"
        else:
            like_type = Like.LikeType.POST
            notification_text = f"{user_liked} has liked your post"

        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        create_notification(
            request,
            to_user=User(post_author),
            notification=notification_text,
            notification_source_type=like_type,
            user_by=signed_in_user,
            post=parent_post,
            comment=parent_comment,
        )
        comment = serializer.save()
        return Response(self.serializer_class(comment).data)


class MessageView(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all()

    def get_queryset(self):
        signed_in_user = self.request.user.id
        return self.queryset.filter(sender_id=signed_in_user) | self.queryset.filter(
            receiver_id=signed_in_user
        )

    def create(self, request, *args, **kwargs):
        user_signed_in = self.request.user.id

        serializer = self.serializer_class(data=self.request.data)

        sender = User.objects.get(pk=user_signed_in)

        serializer.is_valid(raise_exception=True)
        create_notification(
            request,
            to_user=User(self.request.data["receiver"]),
            notification=f"{sender.username} has sent you a message",
            notification_source_type="M",
            user_by=user_signed_in,
            post=None,
            comment=None,
        )
        message = serializer.save()
        return Response(
            self.serializer_class(message).data, status=status.HTTP_201_CREATED
        )
