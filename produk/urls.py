
from django.contrib import admin
from django.urls import path
from produk import views
urlpatterns = [
    path('', views.produk_view, name='product'),
    path('posting/', views.posting, name='productposting'),
    path('edit/<int:id>', views.edit, name='productedit'),
    path('delete/<int:id>', views.delete, name='productdelete'),
]
