from datetime import datetime
from django.db import models
from .DetalleMuestraSismica import DetalleMuestraSismica
class MuestraSismica(models.Model):
    fechaHoraMuestra = models.DateTimeField(null=True, blank=True)
    detallesMuestras = models.ForeignKey(
        DetalleMuestraSismica,
        on_delete=models.CASCADE,
        related_name='muestras_sismicas',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Evento {self.id} - {self.fechaHoraMuestra}"
    
    def obtenerDenominacionYValor(self):
        return self.detallesMuestras.obtenerDenominacionYValor()


