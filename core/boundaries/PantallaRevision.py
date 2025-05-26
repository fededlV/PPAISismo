from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..entities.EventoSismico import *
from ..entities.CambioEstado import *
from ..control.GestorRevision import GestorRevision
from django.shortcuts import render


def habilitarPantalla(request):
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
        return redirect('tomarOpcSeleccionada')
    else:
        # Si se accede por GET, redirigir a la pantalla de selección
        return redirect('tomarOpcSeleccionada')
    
def permitirVisualizarMapa(request): 
    if request.method == 'POST':
        opcion = request.POST.get('opcion')
        if opcion == 'No':
            print("(: No se quiere visualizar el mapa")
            return redirect('permitirModificarDatos')
        else: 
            pass

def tomarRechazoVisualizacion(request): 
    opcion = request.POST.get('opcion')
    gestor = GestorRevision()
    permitir_modificar = gestor.tomarRechazoVisualizacion(opcion)
    print(f"(: Opción seleccionada: {opcion}")
    if permitir_modificar:
        return redirect('permitirModificarDatos')
    else:
        pass

def permitirModificarDatos(request):
    if request.method == 'POST':
        opcion = request.POST.get('opcion')
        if opcion == 'No':
            print("(: No modifican los datos del evento")
            return redirect('solicitarAccion')
        elif opcion == 'Si':
            pass
    # Si es GET, mostrar la pagina con los botones. 
    else:
        return render(request, 'permitirModificarDatos.html')

def tomarRechazoModificacion(request):
    opcion = request.POST.get('opcion')
    gestor = GestorRevision()
    solicitar_accion = gestor.tomarRechazoModificacion(opcion)
    print(f"(: Opción seleccionada: {opcion}")
    if solicitar_accion:
        return redirect('solicitarAccion')
    else:
        pass

def solicitarAccion(request):
    if request.method == 'POST':
        opcion = request.POST.get('opcion')
        if opcion == 'Rechazar':
            print("(: Se solicita la acción de rechazar evento")
            return redirect('tomarEvento')
        elif opcion == 'Validar':
            pass

def tomarAccionRechazarEvento(request):
    opcion = request.POST.get('opcion')
    accionRechazar = GestorRevision.tomarAccionRechazarEvento(opcion)
    print(f"(: Opción seleccionada: {opcion}")
    if accionRechazar:
        print("(: Acción de rechazar evento tomada exitosamente")
        # Redirige a la pantalla en la que se ven los eventos sismicos. 
        return redirect('tomarAccionRechazarEvento')

































    
    




