from django.db import models
import datetime
from django.db import models
from .EstacionSismologica import EstacionSismologica

class Sismografo(models.Model):
    fechaHoraAdquisicion = models.DateTimeField()
    identificadorSismografo = models.CharField(max_length=100)
    nroSerie = models.IntegerField()
    estacion = models.ForeignKey(EstacionSismologica, null=True, blank=True, on_delete=models.SET_NULL)

    def obtenerDatosEstacion(self):
        return self.estacion.getCodigo()