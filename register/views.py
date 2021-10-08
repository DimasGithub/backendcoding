from django.http import response
from django.shortcuts import render
from django.contrib.auth.models import User 

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Seller
from register.serializer import UserSerializer


@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        userSerializer = UserSerializer(data = request.data)
        data = {}
        print(data)
        if userSerializer.is_valid():
            userSerializer.save()
        else:
            data = userSerializer.errors
        return Response(data)  

