from django.db.models import fields
from rest_framework import serializers
from api.models import Seller
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only':True}}
    
    def create(self, validate_data):
        password = validate_data.pop('password')
        user = User(**validate_data)
        user.set_password(password)
        user.save()
        return user
        
