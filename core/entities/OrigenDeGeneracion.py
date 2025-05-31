from django.db import models

class OrigenDeGeneracion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    class Meta:
        app_label = 'core'

    def __str__(self):
        return f"Evento {self.id} - {self.nombre}"
    
    def getDatosOrigen(self):
        return {
            'nombre': self.nombre,
            'descripcion': self.descripcion
        }