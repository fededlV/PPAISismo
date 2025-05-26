from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..entities.EventoSismico import *
from ..entities.CambioEstado import *
from ..control.GestorRevision import GestorRevision
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def tomarOpcSeleccionada(request):
    gestor = GestorRevision()
    EventoSismicosAD = gestor.buscarEventosSismicosAD()
    EventoSismicosAD = gestor.ordenarEventos(EventoSismicosAD)
    return render(request, 'pantallaRevision.html', {'eventos': EventoSismicosAD})

def tomarEvento(request, evento_id=None):
    if request.method == 'POST':
        evento_id = request.POST.get('evento_id')
        gestor = GestorRevision()
        gestor.cambioEstadoBloqueado(evento_id)
        print("(: Evento bloqueado exitosamente")
        mostrarAlcance(request, evento_id)
    else:
        # Si se accede por GET, redirigir a la pantalla de selección
        return redirect('tomarOpcSeleccionada')
    

def mostrarAlcance(request, evento_id):
    evento = get_object_or_404(EventoSismico, id=evento_id)
    alcance = evento.mostrarAlcance()
    return render(request, 'alcanceEvento.html', {'evento': evento, 'alcance': alcance})


def obtenerDatosClasificacion(request, evento_id):
    evento = get_object_or_404(EventoSismico, id=evento_id)
    datos_clasificacion = evento.obtenerDatosClasificacion()
    return render(request, 'datosClasificacion.html', {'evento': evento, 'datos_clasificacion': datos_clasificacion})