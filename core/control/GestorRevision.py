from django.db import models
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponse
from ..entities.EventoSismico import EventoSismico
from typing import List


class GestorRevision:
    @staticmethod
    def tomarEvento(evento_id: int) -> HttpResponse:
        """
        Toma un evento sismico por su ID.
        :param evento_id: ID del evento sismico.
        :return: HttpResponse con el evento sismico.
        """
        from PPAISismo.core.entities.EventoSismico import EventoSismico
        evento = EventoSismico.objects.get(id=evento_id)
        return HttpResponse(f"Evento Sismico tomado: {evento}")

    @staticmethod
    def tomarOpcSeleccionada(opcion: str) -> HttpResponse:
        """
        Toma la opcion seleccionada por el usuario.
        :param opcion: Opcion seleccionada.
        :return: HttpResponse con la opcion seleccionada.
        """
        return HttpResponse(f"Opcion seleccionada: {opcion}")
    
    @staticmethod
    def buscarEventosSismicosAD() -> List:
        """
        Busca eventos sismicos activos en la base de datos.
        :return: Lista de eventos sismicos activos.
        """
        EventoSismicosAD = EventoSismico.obtenerEventosAD()
        EventoSismicosAD = GestorRevision.ordenarEventos(EventoSismicosAD)
        return EventoSismicosAD
    
    @staticmethod
    def getFechaYHoraActual() -> datetime:
        """
        Obtiene la fecha y hora actual.
        :return: Fecha y hora actual.
        """
        return timezone.now()
    
    @staticmethod
    def ordenarEventos(eventos: List[EventoSismico]) -> List[EventoSismico]:
        """
        Ordena los eventos sismicos por fecha y hora de ocurrencia.
        :param eventos: Lista de eventos sismicos.
        :return: Lista de eventos sismicos ordenados.
        """
        eventos.sort(key=lambda x: x.fechaHoraOcurrencia, reverse=True)
        return eventos