from django.shortcuts import render, redirect
from . import models, forms

def home(request):
    consulta_producto = models.Producto.objects.all()
    context = {"productos": consulta_producto}
    return render(request, "producto/index.html", context)

def producto_create(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("producto:home")
    else:  
        form = forms.ProductoForm()
    
    return render(request, "producto/producto_create.html", context={"form": form})

def productocategoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("producto:home")
    else:  
        form = forms.ProductoCategoriaForm()
    
    return render(request, "producto/productocategoria_create.html", context={"form": form})