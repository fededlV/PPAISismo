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