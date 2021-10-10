
from django.contrib import admin
from django.urls import path
from register.views import register_view, login

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', register_view, name='register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
