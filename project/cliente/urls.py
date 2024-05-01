from django.urls import path
from . import views

app_name = 'cliente'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cliente/create/', views.cliente_create, name="cliente_create"),
    path('cliente/nacionalidad/create/', views.nacionalidad_create, name="nacionalidad_create"),
]