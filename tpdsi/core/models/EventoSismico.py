from django.db import models

class EventoSismico(models.Model):
    fechaHoraFin = models.DateTimeField()
    fechaHoraOcurrencia = models.DateTimeField()
    latitudEpicentro = models.FloatField()
    latitudHipocentro = models.FloatField()
    longitudEpicentro = models.FloatField()
    longitudHipocentro = models.FloatField()
    valorMagnitud = models.FloatField()
    estadoActual = models.ForeignKey(Estado, on_delete=models.PROTECT, related_name='eventos_actuales')

    def __str__(self):
        return f"Evento {self.pk} - Magnitud: {self.valorMagnitud} - Estado: {self.estadoActual}"
