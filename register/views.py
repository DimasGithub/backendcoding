from django.shortcuts import render
from django.contrib.auth.models import User 
from register.serializer import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)