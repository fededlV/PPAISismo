from django.db import models
from .Estado import Estado
from typing import List

class EventoSismico(models.Model):
    fechaHoraFin = models.DateTimeField()
    fechaHoraOcurrencia = models.DateTimeField()
    latitudEpicentro = models.FloatField()
    latitudHipocentro = models.FloatField()
    longitudEpicentro = models.FloatField()
    longitudHipocentro = models.FloatField()
    valorMagnitud = models.FloatField()
    estadoActual = models.ForeignKey(Estado, on_delete=models.PROTECT, related_name='eventos_actuales')

    class Meta:
        app_label = 'core'

    @classmethod
    def obtenerEventosAD(cls):
        """
        Obtiene los eventos sismicos activos en la base de datos.
        :return: Lista de eventos sismicos activos.
        """
        eventos_sismicos = cls.objects.all()
        ambito_estado_sismico = []
        for evento in eventos_sismicos:
            a = evento.estadoActual.esAmbitoEventoSismico()
            b = evento.estadoActual.esAutoDetectado()
            if a and b:
                ambito_estado_sismico.append(evento)
        return ambito_estado_sismico

    def bloquear(evento, fechaYHoraActual):
        ceSeleccionado = None
        for ce in cambioEstado.all():
            if ce.esActual():
                ceSeleccionado = ce
        ceSeleccionado.setFechaHoraFin(fechaYHoraActual)
        