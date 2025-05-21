from django.db import models

class DetalleMuestraSismica(models.Model):
    valor = models.IntegerField()
    tipoDato = models.ForeignKey(TipoDato, null=True, blank=True, on_delete=models.SET_NULL)

    def obtenerDenominacionYValor(self):
        if self.tipoDato is not None:
            return self.tipoDato.obtenerDenominacion()
        else:
            return "No tiene tipo de dato registrado"