import datetime
from django.db import models
from .EstacionSismologica import EstacionSismologica

class Sismografo(models.Model):
    fechaHoraAdquisicion = models.DateTimeField()
    identificadorSismografo = models.CharField(max_length=100)
    nroSerie = models.IntegerField()
    estacion = models.ForeignKey(EstacionSismologica, null=True, blank=True)

    def obtenerDatosEstacion(self):
        if self.estacion:
            return self.estacion.getCodigo()
        else:
            return "No tiene estación asociada"
