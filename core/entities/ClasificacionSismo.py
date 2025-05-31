from django.db import models

class ClasificacionSismo(models.Model):
    kmProfundidadDesde = models.FloatField()
    kmProfundidadHasta = models.FloatField()
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"Alcance {self.nombre}"

    def getDatosClasificacion(self):
        return {
            'kmProfundidadDesde': self.kmProfundidadDesde,
            'kmProfundidadHasta': self.kmProfundidadHasta,
            'nombre': self.nombre
        }
    