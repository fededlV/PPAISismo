from django.db import models

class DetalleMuestraSismica(models.Model):
    valor = models.IntegerField()
    tipoDato = models.ForeignKey('TipoDeDato', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        app_label = 'core'

    def obtenerDenominacionYValor():
        pass

