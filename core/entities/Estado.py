from django.db import models

class Estado(models.Model):
    ambito = models.CharField(max_length=100)
    nombreEstado = models.CharField(max_length=100)

    #6. Listo
    def ambitoEventosSismico(self):
        return self.ambito == "EventoSismico"
    
    #7. Listo
    def esAutoDetectado(self):
        return self.nombreEstado == "AutoDetectado"

    def esBloqueado(self):
        return self.nombreEstado == "Bloqueado"

    def esRechazado(self):
        return self.nombreEstado == "Rechazado"

    class Meta:
        app_label = 'core'

