from django.shortcuts import render, redirect
from . import models, forms

def home(request):
    consulta_cliente = models.Cliente.objects.all()
    context = {"clientes": consulta_cliente}
    return render(request, "cliente/index.html", context)

def nacionalidad_create(request):
        if request.method == "POST":
            form = forms.NacionalidadForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect("cliente:home")
        else:  
            form = forms.NacionalidadForm()
        
        return render(request, "cliente/nacionalidad_create.html", context={"form": form})

def cliente_create(request):
        if request.method == "POST":
            form = forms.ClienteForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect("cliente:home")
        else:  
            form = forms.ClienteForm()
        
        return render(request, "cliente/cliente_create.html", context={"form": form})

