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
    def tomarOpcSeleccionada(opcion: str) -> HttpResponse:
        """
        Toma la opcion seleccionada por el usuario.
        :param opcion: Opcion seleccionada.
        :return: HttpResponse con la opcion seleccionada.
        """
        return HttpResponse(f"Opcion seleccionada: {opcion}")
    
    # cambiar el nombre a buscarEventosSismicos( )
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
    def mostrarDatosEventos(): pass
    
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

    # cambiar el nombre a obtenerFechaHoraActual()
    @staticmethod
    def getFechaYHoraActual() -> datetime:
        """
        Obtiene la fecha y hora actual.
        :return: Fecha y hora actual.
        """
        return timezone.now()
    
    # cambiar el nombre a bloquearEvento()
    @staticmethod
    def cambioEstadoBloqueado(eventoBloqueado: EventoSismico) -> None:
        """
        Cambia el estado de un evento sismico a bloqueado.
        :param eventoBloqueado: Evento sismico a bloquear.
        :param fechaYHoraActual: Fecha y hora actual.
        """
        GestorRevision.buscarEstadoBloqueado(eventoBloqueado)
        GestorRevision.getFechaYHoraActual()
        return eventoBloqueado.alcance.getDatosAlcance()
    
    @staticmethod
    def mostrarAlcance(evento: EventoSismico) -> dict:
        """
        Muestra el alcance del evento sismico.
        :param evento: Evento sismico.
        :return: Diccionario con los datos del alcance del evento sismico.
        """
        return evento.alcance.getDatosAlcance()

    # cambiar el nombre a obtenerClasificacion()
    @staticmethod
    def obtenerDatosClasificacion(evento: EventoSismico) -> dict:
        """
        Obtiene los datos de la clasificación del evento sismico.
        :param evento: Evento sismico.
        :return: Diccionario con los datos de la clasificación del evento sismico.
        """
        return evento.obtenerDatosClasificacion()
    
    @staticmethod
    def obtenerOrigen() : pass
    
    @staticmethod
    def obtenerDatosEstacion() : pass
    
    @staticmethod
    def clasificarPorEstacion() : pass
    
    @staticmethod
    def llamarCU18() -> str:
        return "Llamando CU 18"
    
    @staticmethod
    def validarExistenciaDatos() : pass
    
    @staticmethod
    def validarAccionSeleccionada(): pass
    
    @staticmethod
    def registrarRechazoEvento(): pass
    
    @staticmethod
    def obtenerEmpleadoLogueado(): pass
    
    @staticmethod
    def obtenerFechaHoraActual() -> datetime:
        return timezone.now()
    
    @staticmethod
    def buscarEstadoRechazado(): pass
    
    @staticmethod
    def registrarRevision(): pass
    
    @staticmethod
    def finCU() -> str:
        return "Fin de CU"