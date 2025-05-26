from django.db import models
from .Usuario import Usuario  # Importa Usuario si están en el mismo paquete

class Empleado(models.Model):
    apellido = models.CharField(max_length=100)
    mail = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    logueado = models.BooleanField(default=False)

    class Meta:
        app_label = 'core'
