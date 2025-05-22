from django.shortcuts import render
from datetime import datetime
from .entities.EventoSismico import EventoSismico
# Create your views here.

def home(request):
    return render(request, 'home.html')

# secundario (borrar comentario)
def ordenarEventos(eventos):
    eventos.sort(key=lambda x: x.fechaHoraOcurrencia, reverse=True)
    return eventos

def getFechaYHoraActual():
    return datetime.now()



# self

def buscarEventosSismicos():
    EventoSismicosAD = EventoSismico.obtenerEventosAD()
    EventoSismicosAD = ordenarEventos(EventoSismicosAD)
    return render(request, 'pantallaRevision.html', {'eventos': EventoSismicosAD})

def buscarEstadoBloqueado(evento):
    # Tomar todos los estados del evento
    estados = evento.obtenerEstados()

    for estado in estados:
        if estado.esAmbitoEventoSismico():
            if estado.esBloqueado():
                return estado
    return None

def bloquearEvento(eventoBloqueado, fechaYHoraActual):
    


    
# Tomar 
def tomarOpcSeleccionada(request):
    return buscarEventosSismicos()

def tomarEvento(request, evento):
    eventoBloqueado = buscarEstadoBloqueado(evento)
    fechaYHoraActual = getFechaYHoraActual()
    bloquearEvento(eventoBloqueado, fechaYHoraActual)