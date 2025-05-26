from django.db import models

class OrigenDeGeneracion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    class Meta:
        app_label = 'core'

    
    def getDatosOrigen(self):
        return {
            'nombre': self.nombre,
            'descripcion': self.descripcion
        }