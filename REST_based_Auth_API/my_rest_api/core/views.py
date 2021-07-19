import json

from django.db.models.expressions import OrderBy
from django.http import request
from django.shortcuts import render

from rest_framework import status
from rest_framework import serializers,viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User

from .models import Comment, Post, Request
from .serializers import make_comment_serializer, user_serializer, make_post_serializer, send_request_serializer, change_request_status



class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {"message" : "Hello Faraz!"}
        return Response(content)


class RegisterUser(viewsets.ModelViewSet):
    serializer_class= user_serializer
    permission_classes=(IsAuthenticated,)
    #queryset = User.objects.all()

    @action(methods=["Post"],detail=True)
    def get_queryset(self):
        print("hello")
        serializer = user_serializer(data=self.request.data)
        serializer_is_valid=serializer.is_valid(raise_exception=True)
        if serializer_is_valid:
            user = serializer.save()
            if user:
                return User.objects.filter().order_by('-id')[:1]
        
        return None
        
  
class GetUsers(viewsets.ModelViewSet):
    serializer_class= user_serializer
    permission_classes=(IsAuthenticated,)
    queryset = User.objects.all()


class MakePost(viewsets.ModelViewSet):
    serializer_class= make_post_serializer
    permission_classes=(IsAuthenticated,)
    #queryset = User.objects.all()

    @action(methods=["Post"],detail=True)
    def get_queryset(self):
        serializer = make_post_serializer(data=self.request.data)
        serializer_is_valid=serializer.is_valid(raise_exception=True)
        if serializer_is_valid:
            user = serializer.save()
            if user:
                return Post.objects.filter().order_by('-id')[:1]
        
        return None


class MakeComment(viewsets.ModelViewSet):
    serializer_class= make_comment_serializer
    permission_classes=(IsAuthenticated,)
    #queryset = User.objects.all()

    @action(methods=["Post"],detail=True)
    def get_queryset(self):
        print("hello")
        serializer = make_comment_serializer(data=self.request.data)
        serializer_is_valid=serializer.is_valid(raise_exception=True)
        if serializer_is_valid:
            user = serializer.save()
            if user:
                return Comment.objects.filter().order_by('-id')[:1]
        
        return None

 
class SendRequest(viewsets.ModelViewSet):
    serializer_class= send_request_serializer
    permission_classes=(IsAuthenticated,)
    #queryset = User.objects.all()

    @action(methods=["Post"],detail=True)
    def get_queryset(self):
        friend_request_exists = Request.objects.filter(requestee_id=self.request.data['requestee'])
        if friend_request_exists.exists():
            return None
        serializer = send_request_serializer(data=self.request.data)
        serializer_is_valid=serializer.is_valid(raise_exception=True)
        if serializer_is_valid:
            request = serializer.save()
            if request:
                return Request.objects.filter().order_by('-id')[:1]
        
        return None


class GetRequest(viewsets.ModelViewSet):
    serializer_class= send_request_serializer
    permission_classes=(IsAuthenticated,)

    @action(methods=["get"],detail=True)
    def get_queryset(self):  
        requests_data = None
        
        data_dictionary = json.loads(self.request.body)
        requestee_or_requestor = []

        for key in data_dictionary.keys():
            requestee_or_requestor.append(key)
            
        if requestee_or_requestor[0]=='requestee':
            requests_data = Request.objects.filter(requestee_id=int(self.request.data['requestee']))  
        elif requestee_or_requestor[0]=='requestor':
            requests_data = Request.objects.filter(requestor_id=int(self.request.data['requestor']))
        return requests_data
        

class ChangeStatus(viewsets.ModelViewSet):
    serializer_class= send_request_serializer
    permission_classes=(IsAuthenticated,)
    
    @action(methods=["Put"],detail=True)
    def get_queryset(self):
        #if(self.request.data['status']=='Rejected'):
        data = Request.objects.filter(pk=self.request.data['id']).update(status=self.request.data['status'])
            #Request.objects.filter(pk=self.request.data['id']).delete()
        return Request.objects.filter(pk=self.request.data['id'])
        