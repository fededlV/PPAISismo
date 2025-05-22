from django.shortcuts import render
from .entities.EventoSismico import EventoSismico
# Create your views here.

def home(request):
    return render(request, 'home.html')

def ordenarEventos(eventos):
    eventos.sort(key=lambda x: x.fechaHoraOcurrencia, reverse=True)
    return eventos

def buscarEventosSismicos():
    EventoSismicosAD = EventoSismico.obtenerEventosAD()
    EventoSismicosAD = ordenarEventos(EventoSismicosAD)
    return render(request, 'pantallaRevision.html', {'eventos': EventoSismicosAD})

def buscarEstadoBloqueado(estados):
    for estado in estados:
        if estado.esAmbitoEventoSismico():
            if estado.esBloqueado():
                return estado
    return None


    
# Tomar 

def tomarOpcSeleccionada(request):
    return buscarEventosSismicos()

def tomarEvento(request, id):
    buscarEventosSismicos()