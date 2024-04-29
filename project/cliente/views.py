from django.shortcuts import render, redirect
from . import models

def home(request):
    return render(request, "cliente/index.html")
