from django.db import models
from .Sismografo import Sismografo

class SerieTemporal(models.Model):
    condicionAlarma = models.BooleanField()
    fechaHoraInicioRegistroMuestras = models.DateTimeField()
    fechaHoraRegistro = models.DateTimeField()
    frecuenciaMuestreo = models.FloatField()
    sismografo = models.ForeignKey(
        Sismografo,
        on_delete=models.CASCADE,
        related_name='series_temporales'
    )

    def obtenerDatosMuestras(self):
        pass

    def obtenerDatosEstacion(self):
        return self.sismografo.obtenerDatosEstacion()
    
    