from django.urls import path
from . import views

app_name = 'cliente'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cliente/create/', views.cliente_create, name="cliente_create"),
]