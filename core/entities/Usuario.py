from django.db import models
from .Empleado import Empleado  # Usa import relativo si están en el mismo paquete

class Usuario(models.Model):
    contrasena = models.CharField(max_length=128)
    nombreUsuario = models.CharField(max_length=150, unique=True)
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        app_label = 'core'

    def getAsLogueado(self):
        empleado = getattr(self, 'empleado', None)
        if empleado and empleado.logueado:
            return empleado
        return None
