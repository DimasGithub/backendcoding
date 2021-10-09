
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('product/', views.product_view, name='product'),
    path('product/<int:id>', views.product_detail_view, name='detailproduct'),
]
