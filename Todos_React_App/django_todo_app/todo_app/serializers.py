from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Todo

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({"user": self.user.username})
        data.update({"id": self.user.id})
        # and everything else you want to send in the response
        return data

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id","todo_text"]