from django.db import models
from .Sismografo import Sismografo
from .MuestraSismica import MuestraSismica
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
    muestraSismica = models.ForeignKey(
        MuestraSismica,
        on_delete=models.CASCADE,
        related_name='series_temporales',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Evento {self.id} - {self.fechaHoraInicioRegistroMuestras} - {self.sismografo}"
    
    # 39
    def obtenerDatosMuestras(self):
        return [muestra.obtenerDenominacionYValor() for muestra in self.muestraSismica.all()]

    def obtenerDatosEstacion(self):
        return self.sismografo.obtenerDatosEstacion()

