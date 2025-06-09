from django.db import models
from .Sismografo import Sismografo
from .MuestraSismica import MuestraSismica


class SerieTemporal(models.Model):
    condicionAlarma = models.BooleanField()
    fechaHoraInicioRegistroMuestras = models.DateTimeField()
    fechaHoraRegistro = models.DateTimeField()
    frecuenciaMuestreo = models.FloatField()
    muestraSismica = models.ForeignKey(
        MuestraSismica,
        on_delete=models.CASCADE,
        related_name='series_temporales',
        null=True,
        blank=True
    )
    

    def __str__(self):
        return f"Evento {self.id} - {self.fechaHoraInicioRegistroMuestras}"
    
    # 39
    def obtenerDatosMuestras(self):
        if self.muestraSismica:
            return [self.muestraSismica.obtenerDenominacionYValor()]
        else:
            return []

    # 45
    def obtenerDatosEstacion(self, sismografo: Sismografo): #Dependencia con sismografo. 
        return sismografo.obtenerDatosEstacion()

