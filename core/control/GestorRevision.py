from django.db import models
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponse
from ..entities.EventoSismico import EventoSismico
from typing import List


class GestorRevision:
    eventosSeleccionadosAd = []
    eventoSeleccionado = None

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
    
    @staticmethod
    def buscarEstadoBloqueado(evento: EventoSismico):
        """
        Busca el estado bloqueado de un evento sismico.
        :param evento: Evento sismico.
        :return: Estado bloqueado del evento sismico.
        """
        from ..entities.Estado import Estado
        estados = Estado.objects.all()
        for estado_obj in estados:
            if estado_obj.esAmbitoEventoSismico() and estado_obj.esBloqueado():
                return estado_obj
        return None

    @staticmethod
    def cambioEstadoBloqueado(eventoBloqueado: EventoSismico) -> None:
        """
        Cambia el estado de un evento sismico a bloqueado.
        :param eventoBloqueado: Evento sismico a bloquear.
        :param fechaYHoraActual: Fecha y hora actual.
        """
        buscarEstado = GestorRevision.buscarEstadoBloqueado(eventoBloqueado)
        fechaYHoraActual = GestorRevision.getFechaYHoraActual()

    @staticmethod
    def tomarRechazoVisualizacion(opcion: str) -> bool:
        """ 
        Procesa el rechazo de visualización de un evento sismico.
        :param opcion: Opción seleccionada por el usuario.
        :return: True si la opción Visualizar, False en caso contrario.
        """
        if opcion == "Rechazar":
            print("(: Opción seleccionada: Rechazar")
            return True
        return False
    
    @staticmethod
    def tomarRechazoModificacion(opcion: str) -> bool:
        if opcion == "Rechazar":
            print("(: Opción seleccionada: Rechazar")
            return True
        return False
    
    @staticmethod
    def tomarRechazoModificacion(opcion: str) -> bool:
        """
        Procesa el rechazo de modificación de un evento sismico.
        :param opcion: Opción seleccionada por el usuario.
        :return: True si la opción es "Si", False en caso contrario.
        """
        if opcion == "Si":
            print("(: Opción seleccionada: Si")
            return True
        return False
    
    @staticmethod
    def tomarAccionRechazarEvento(opcion: str) -> bool:
        """
        Procesa la acción de rechazar un evento sismico.
        :param opcion: Opción seleccionada por el usuario.
        :return: True si la opción es "Rechazar", False en caso contrario.
        """
        if opcion == "Rechazar":
            print("(: Opción seleccionada: Rechazar")
            return True
        return False
