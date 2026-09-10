from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=20, default='P000')
    nombre = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

