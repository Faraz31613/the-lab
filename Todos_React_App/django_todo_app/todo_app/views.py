from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .serializers import MyTokenObtainPairSerializer, TodoSerializer


from .models import Todo


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class Todo(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = (AllowAny,)
    queryset = Todo.objects.all()
