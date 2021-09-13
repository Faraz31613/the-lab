from django.contrib.auth import models
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenVerifySerializer
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
from django.shortcuts import get_object_or_404

from .models import Comment, Like, Message, Notification, Post, Request, Friend


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({"f_name": self.user.first_name})
        data.update({"l_name": self.user.last_name})
        data.update({"user": self.user.username})
        data.update({"id": self.user.id})

        # and everything else you want to send in the response
        return data

# class MyTokenVerifySerializer(TokenVerifySerializer):
#     pass


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'], first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'])
        return user

    class Meta:
        model = User
        fields = ("id", "username", "email",
                  "password", "first_name", "last_name")


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")


class HomeSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    is_liked = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = ("id", "text_post", "user","is_liked")

    def get_is_liked(self, post):
        signed_in_user_Id = self.context['request'].user.id
        try:
            get_object_or_404(Like,post=post.id,user=signed_in_user_Id)
            return True
        except:
            return False
    


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "text_post", "user")    



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "comment", "user", "post", "comment_text")


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


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "sender", "message", "receiver")
