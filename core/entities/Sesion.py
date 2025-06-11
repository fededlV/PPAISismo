from django.db import models
from .Usuario import Usuario
from .Empleado import Empleado

class Sesion(models.Model):
    """
    Modelo de Sesion que representa una sesión de usuario en la aplicación.
    """
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='sesiones')
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)

    def getUsuarioLogueado(self) -> Empleado:
        """
        Devuelve el usuario asociado a la sesión.
        """
        return self.usuario.getAsLogueado()