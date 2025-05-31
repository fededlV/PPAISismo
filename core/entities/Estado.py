from django.db import models

class Estado(models.Model):
    ambito = models.CharField(max_length=100)
    nombreEstado = models.CharField(max_length=100)

    # 6, 16 Ambito eventos sismicos
    def ambitoEventoSismico(self):
        return self.ambito == "EventoSismico"

    # 7 Es auto detectado
    def esAutoDetectado(self):
        print(self.nombreEstado)
        return self.nombreEstado == "AutoDetectado"

    # 17 Es bloqueado
    def esBloqueado(self):
        return self.nombreEstado == "Bloqueado"

    def esRechazado(self):
        return self.nombreEstado == "Rechazado"

    class Meta:
        app_label = 'core'

