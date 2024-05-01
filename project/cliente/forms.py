from django import forms
from . import models

class NacionalidadForm(forms.ModelForm):
    class Meta:
        model = models.Nacionalidad
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
            "apellido": forms.TextInput(attrs={"class": "form-control", "placeholder": "Apellido"}),
            "nacionalidad": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nacionalidad"}),
            "direccion": forms.TextInput(attrs={"class": "form-control", "placeholder": "Dirección"}),
            # "telefono": forms.IntegerField(attrs={"class": "form-control", "placeholder": "Teléfono"}),
            "mail": forms.TextInput(attrs={"class": "form-control", "placeholder": "Mail"}),
        }