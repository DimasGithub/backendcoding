
from django.contrib import admin
from django.urls import path
from register import views
urlpatterns = [
    path('register', views.UserCreate.as_view())
]
