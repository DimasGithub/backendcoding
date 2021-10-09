from api.models import Product, Category

from rest_framework import serializers



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    categoryku  = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'