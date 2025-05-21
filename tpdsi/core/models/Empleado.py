from django.db import models

class Empleado(models.Model):
    apellido = models.CharField(max_length=100)
    mail = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    logueado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"