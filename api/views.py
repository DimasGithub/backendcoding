from django.http import response
from django.shortcuts import render
from django.contrib.auth.models import User
from api import serializer 

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated  # <-- Here
from rest_framework import filters

from api.models import Product, Category
from api.serializer import ProductSerializer

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

class ProductAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    filter_backends = (DynamicSearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['POST', 'GET'])

def product_view(request):
    permission_classes = (IsAuthenticated,) 
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
    if request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return serializer.errors
    return Response(serializer.data)


@api_view(['PUT', 'GET', 'DELETE'])

def product_detail_view(request,id):
    permission_classes = (IsAuthenticated,) 
    query = Product.objects.get(id=id)
    query2 = Product.objects.filter(id=id)
    if request.method == 'GET':
        data = ProductSerializer(query2, many=True)
        return Response(data.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(query, data= request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['message'] = "data berhasil diubah"
            return Response(data)
        else:
            data = serializer.errors
            return Response(data)
    elif request.method == 'DELETE':
        serializer = Product.objects.get(id=id)
        serializer.delete()
        data = {}
        data['message'] = "data berhasil di hapus"
        return Response(data)

