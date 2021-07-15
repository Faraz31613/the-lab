from django.shortcuts import render

from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User

from .models import Post
from .serializers import UserSerializer, MakePostSerializer



class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {"message" : "Hello Faraz!"}
        return Response(content)


class RegisterUser(APIView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        serializer_is_valid=serializer.is_valid(raise_exception=True)
        if serializer_is_valid:
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

class GetUsers(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        users={}
        key=1
        for username in User.objects.all():
            users[str(key)] = str(username)
            key=key+1
        
        return Response(users)

class MakePost(APIView):
    permission_classes = (AllowAny,)

    def post(self,request,format='json'):
        serializer = MakePostSerializer(data=request.data)
        
        serializer_is_valid=serializer.is_valid(raise_exception=True)
        if serializer_is_valid:
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


