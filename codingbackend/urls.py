
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from codingbackend import views
urlpatterns = [
    path('', views.index, name= "index" ),
    path('admin/', admin.site.urls),
    path('account/',include(('register.urls', 'register'), namespace='register')),
    path('api/',include(('api.urls', 'api'), namespace='api')),
    path('product/', include(('produk.urls', 'produk'), namespace='produk')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
