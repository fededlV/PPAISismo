from django.db import models

class TipoDeDato(models.Model):
    denominacion = models.CharField(max_length=100)
    nombreUnidadMedida = models.CharField(max_length=100)
    valorUmbral = models.FloatField()

    def obtenerDenominacionYValor(self): 
        return f"{self.denominacion} ({self.valorUmbral})"

    def getDenominacion(self):
        return self.denominacion

    def getValorUmbral(self):
        return self.valorUmbral

    def __str__(self):
        return self.denominacion