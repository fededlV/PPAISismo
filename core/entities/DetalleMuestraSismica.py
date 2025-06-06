from django.db import models
from .TipoDeDato import TipoDeDato
class DetalleMuestraSismica(models.Model):
    valor = models.IntegerField()
    tipoDato = models.ForeignKey(TipoDeDato,on_delete=models.CASCADE,related_name='detalles_muestras_sismicas',null=True, blank=True)

    def __str__(self):
        return f"Evento {self.id} - {self.valor}"
    class Meta:
        app_label = 'core'
    
    # 41
    def obtenerDenominacionYValor(self):
        return self.tipoDato.obtenerDenominacionYValor()

