from django.db import models

class OrigenDeGeneracion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def getDatosOrigen(self):
        return nombre, descripcion
