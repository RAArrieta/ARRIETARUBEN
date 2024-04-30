from django.db import models

class Nacionalidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    mail = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    nacionalidad_id =models.ForeignKey(Nacionalidad, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
