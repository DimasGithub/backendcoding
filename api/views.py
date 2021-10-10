from django_filters import FilterSet, AllValuesFilter, DateTimeFilter, NumberFilter 
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
from rest_framework.filters import SearchFilter, OrderingFilter


from api.models import Product, Category
from api.serializer import ProductSerializer

class DynamicSearchFilter(SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', ['product_title', 'product_desc', 'category_id__category_title'])

class DynamicOrderingFilter(OrderingFilter):
    def get_ordering_fields(self, view, request):
        return request.GET.getlist('ordering_fields', ['product_title', 'product_price', 'category_id'])

class ProductAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    filter_backends = (DynamicSearchFilter, DynamicOrderingFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    ordering = ['product_title', 'product_price', 'category_id']

@api_view(['POST', 'GET'])
@permission_classes([AllowAny,])
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
@permission_classes([AllowAny,])
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

