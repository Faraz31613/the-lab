from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueTogetherValidator

from .models import Comment, Notification, Post, Request, Friend


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({"user": self.user.username})
        data.update({"id": self.user.id})
        # and everything else you want to send in the response
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "text_post", "user")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "comment", "post")


class RequestSerializer(serializers.ModelSerializer):
    validators = [
        UniqueTogetherValidator(
            queryset=Request.objects.filter(status="P" or "R"),
            fields=["requestor", "status", "requestee"],
        )
    ]

    class Meta:
        model = Request
        fields = ("id", "requestor", "status", "requestee")


class ChangeRequestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ("id", "status", "requestee", "requestor")


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ("user", "friend", "status")


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
