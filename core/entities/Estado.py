from django.db import models

class Estado(models.Model):
    ambito = models.CharField(max_length=100)
    nombreEstado = models.CharField(max_length=100)

    # cambiar nombre AmbitoEventoSismico()
    def esAmbitoEventoSismico(self):
        return self.ambito == "EventoSismico"

    def esAutoDetectado(self):
        return self.nombreEstado == "AutoDetectado"

    def esBloqueado(self):
        return self.nombreEstado == "Bloqueado"

    # cambiar nombre esRechazar()
    def esRechazado(self):
        return self.nombreEstado == "Rechazado"

    class Meta:
        app_label = 'core'

