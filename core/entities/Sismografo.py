from django.db import models
import datetime
from django.db import models
from .EstacionSismologica import EstacionSismologica

class Sismografo(models.Model):
    fechaHoraAdquisicion = models.DateTimeField()
    identificadorSismografo = models.CharField(max_length=100)
    nroSerie = models.IntegerField()
    estacion = models.ForeignKey(EstacionSismologica, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"Evento {self.id} - {self.identificadorSismografo} - {self.estacion}"
    
    def obtenerDatosEstacion(self):
        return self.estacion.getCodigo()