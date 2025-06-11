from django.db import models
from .Empleado import Empleado  # Usa import relativo si están en el mismo paquete

class Usuario(models.Model):
    contrasena = models.CharField(max_length=128)
    nombreUsuario = models.CharField(max_length=150, unique=True)
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Evento {self.id} - {self.nombreUsuario}"
    class Meta:
        app_label = 'core'

    def getAsLogueado(self) -> dict:
        return self.empleado
