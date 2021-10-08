from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from api.models import Seller

# class RegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(style = {'input_type':'password'}, write_only = True)
#     class Meta:
#         model = Seller
#         fields = ['seller_name', 'seller_email','seller_phone_number', 'password']
#         extra_kwargs = {
#             'password' : {'write_only ': True}
#         }
#     def save(self):
#         account = Seller(
#             username = self.validated_data['seller_name'], 
#             seller_email = self.validated_data['seller_email'], 
#             seller_phone_number = self.validated_data['seller_phone_number'])
#         account.save()
#         return account

class UserSerializer(serializers.ModelSerializer):
    seller_phone_number = serializers.CharField(max_length=12)
    password = serializers.CharField(style = {'input_type':'password'}, write_only = True)
    class Meta:
        model = User
        fields = ['username','email', 'password', 'seller_phone_number']
        extra_kwargs = {
            'password' : {'write_only ': True}
        }
    def save(self):
        sel = Seller(
            seller_name = self.validated_data['username'],
            seller_email = self.validated_data['email'],
            seller_phone_number = self.validated_data['seller_phone_number'],
        )
        sel.save()
        user = User.objects.create_user(
            username = self.validated_data['username'], 
            email = self.validated_data['email'],
            password = self.validated_data['password'] )
        user.set_password(user.password)
        user.save()
        return user 