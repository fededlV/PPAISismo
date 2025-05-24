from django.shortcuts import render
from datetime import datetime
from .entities.EventoSismico import EventoSismico


# Create your views here.


# self



def buscarEstadoBloqueado(evento):
    # Tomar todos los estados del evento
    estados = evento.obtenerEstados()

    for estado in estados:
        if estado.esAmbitoEventoSismico():
            if estado.esBloqueado():
                return estado
    return None

def bloquearEvento(eventoBloqueado, fechaYHoraActual):
    pass


    
# Tomar 

def tomarEvento(request, evento):
    eventoBloqueado = buscarEstadoBloqueado(evento)
    fechaYHoraActual = getFechaYHoraActual()
    bloquearEvento(eventoBloqueado, fechaYHoraActual)
    print("Evento bloqueado:", eventoBloqueado)
    pass