from django.shortcuts import render
from models import EventoSismico
# Create your views here.

def buscarventosSismicos(request):
    EventosSismicosAD = EventoSismico.obtenerEventosAD()
    return render(request, 'pantallaRevicion.html', {'grillaEventos': EventosSismicosAD}) 