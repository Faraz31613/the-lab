from typing import Any
from django.db.models import fields
from django.db.models.base import Model
from django.http import request
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

from .models import Comment, Post, Request

class user_serializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class make_post_serializer(serializers.ModelSerializer):
    text_post = serializers.CharField(max_length=500)

    def add_post(self,validated_data):
        post = Post.objects.create(validated_data['text_post'])
        return post

    class Meta:
        model = Post
        fields = ('id','text_post','user')

class make_comment_serializer(serializers.ModelSerializer):
    comment = serializers.CharField(max_length=300)
    
    def add_comment(self,validated_data):
        comment = Comment.objects.create(validated_data['comment'])
        return comment

    class Meta:
        model = Comment
        fields = ('id','comment','post')

class send_request_serializer(serializers.ModelSerializer):
    status =serializers.CharField(max_length=30)
    requestee = [UniqueValidator(queryset=Request.objects.all())]
            
    # requestor = serializers.IntegerField(
    #         required=True,
    #         )

    def add_request(self,validated_data):
        request = Request.objects.create(validated_data['status'],validated_data['requestee'])
        return request

    class Meta:
        model = Request
        fields = ('id','requestor','status','requestee')

class change_request_status(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = ('id','requestor','status','requestee')