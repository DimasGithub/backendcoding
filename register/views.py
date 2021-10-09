from django.http import response
from django.shortcuts import render
from django.contrib.auth.models import User 

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token

from api.models import Seller
from register.serializer import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    if request.method == 'POST':
        userSerializer = UserSerializer(data = request.data)
        if userSerializer.is_valid():
            user = userSerializer.save()
            token = Token.objects.get_or_create(user=user)[0].key
            data={}
            data['message'] = 'Seller Berhasil Registrasi'
            data['username'] = user.username
            data['email'] = user.email
            data['token'] = token
        else:
            data = userSerializer.errors
        return Response(data)  
