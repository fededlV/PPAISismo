from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..entities.EventoSismico import *
from ..entities.CambioEstado import *
from ..control.GestorRevision import GestorRevision
from django.shortcuts import render

#1. Listo
def opcRegistrarResRevisionMan(request):
    gestor = GestorRevision()
    eventosSismicosAd = gestor.tomarOpcSeleccionada()
    return render(request, 'pantallaRevision.html', {'eventos': eventosSismicosAd})

#2. Listo
def habilitarPantalla(request):
    return render(request, 'home.html')

#11. Listo 
def mostrarEventosAD(request):
    gestor = GestorRevision()
    # Supón que tienes una función para obtener todos los eventos
    eventos = gestor.tomarOpcSeleccionada(gestor) #ACA NO SE SI ES ASI O SE TENDRIA QUE SUSTITUIR EL METODO QUE IMPLEMENTA EL TOMAROPCSELECCIONADA POR MOSTRARDATOS.
    # Ahora gestor.eventosSismicosAd es una lista de diccionarios ordenados
    return render(request, 'pantallaRevision.html', {'eventos': eventos})

#12. Listo
def solicitarSeleccion():pass

#13. Listo
def tomarEvento(request):
    if request.method == 'POST':
        seleccionado = request.POST.get("evento_seleccionado")
        if seleccionado: 
            fecha, lat, lon = seleccionado.split('|')
            gestor = GestorRevision()
            gestor.tomarOpcSeleccionada() # Esto lo que hace es que se cargue la lista de eventos sismicos activos en la base de datos.
            eventoSel = gestor.tomarEvento(fecha, lat, lon)
        
        return mostrarAlcance(eventoSel) #Esto hay q cambiarlo 
    else:
        # Si se accede por GET, redirigir a la pantalla de selección
        return HttpResponse('Esta vista solo admite solicitudes POST')
    
def mostrarAlcance():
    return mostrarClasificacion()

def mostrarClasificacion():
    return mostrarDatosOrigen()

def mostrarDatosOrigen(): 
    return permitirVisualizarMapa()
    
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
            # return redirect('tomarEvento1')
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









































