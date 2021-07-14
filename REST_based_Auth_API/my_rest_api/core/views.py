from django.shortcuts import render

from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.contrib.auth.models import User



class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {"message" : "Hello Faraz!"}
        return Response(content)


class RegisterUser(APIView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        print(request.data)
        serializer_is_valid=serializer.is_valid(raise_exception=True)
        print(serializer_is_valid)
        if serializer_is_valid:
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

        
    


