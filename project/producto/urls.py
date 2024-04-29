from django.urls import path
from . import views

app_name = 'producto'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('producto/create/', views.producto_create, name="producto_create"),
    path('productocategoria/create/', views.productocategoria_create, name="productocategoria_create"),
]
