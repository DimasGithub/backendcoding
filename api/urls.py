
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('apishipping/', views.viewsprice, name= 'shippingprice'),
    path('shipping/', views.shipping, name='shipping'),
    path('product/', views.product_view, name='product'),
    path('product/<int:id>', views.product_detail_view, name='detailproduct'),
    path('product/cari/', views.ProductAPIView.as_view(), name='searchproduct'),
]
