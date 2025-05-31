from django.db import models

class DetalleMuestraSismica(models.Model):
    valor = models.IntegerField()
    tipoDato = models.ForeignKey('TipoDeDato', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Evento {self.id} - {self.valor}"
    class Meta:
        app_label = 'core'

    def obtenerDenominacionYValor():
        pass

