from django.db import models

class ProductoCategoria(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    categoria_id = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.precio}"
