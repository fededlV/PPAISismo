from django.db import models

class Estado(models.Model):
    ambito = models.CharField(max_length=100)
    nombreEstado = models.CharField(max_length=100)

    def ambitoEventoSismico(self, eventoSismico):
        return eventoSismico.estado == self.nombreEstado

    def esAutoDetectado(self):
        return self.nombreEstado == "AutoDetectado"

    def esBloqueado(self):
        return self.nombreEstado == "Bloqueado"

    def esRechazado(self):
        return self.nombreEstado == "Rechazado"

    def __str__(self):
        return f"{self.nombreEstado} ({self.ambito})"
