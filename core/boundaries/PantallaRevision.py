from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..entities.EventoSismico import *
from ..entities.CambioEstado import *
from ..control.GestorRevision import GestorRevision
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
import json

class PantallaRevision:
    def __init__(self):
        self.gestor = GestorRevision()
        self.alcance = None
        self.clasificacion = None
        self.origen = None
        
    # 1 Opcion Registrar Res Revicion Manual
    def opcRegistrarResRevisionMan(self, request):
        gestor = GestorRevision()
        eventosSismicosAd = gestor.tomarOpcSeleccionada()
        return render(request, 'pantallaRevision.html', {'eventos': eventosSismicosAd})
    
    # 2
    def habilitarPantalla():
        return "Pantalla habilitada"

    # 11
    def mostrarEventosAD():
        pass

    # 12
    def solicitarSeleccion():
        pass

    # 13 Tomar eventos seleccionado
    def tomarEvento(self, request):
        if request.method == 'POST':
            evento_id = request.POST.get('evento_id')
            eventoTomado = self.gestor.tomarEvento(evento_id) # LLamo al 14 del gestor
            self.mostrarAlcance()  # Usamos el método separado
            self.mostrarClasificacion()  # Usamos el método separado
            self.mostrarDatosOrigen()  # Usamos el método separado
            return render(request, 'pantallaRevision.html', {
                'eventos': None,
                'alcance': self.alcance,
                'clasificacion': self.clasificacion,
                'origen': self.origen
            })
        else:
            # Si se accede por GET, redirigir a la pantalla de selección
            return redirect('tomarOpcSeleccionada')
        
    # 28 mostrar alcance
    def mostrarAlcance(self) -> None:
        self.alcance = self.gestor.eventoSismicoSeleccionado.mostrarAlcance()
        
    # 32 mostrar clasificacion
    def mostrarClasificacion(self) -> None:
        self.clasificacion = self.gestor.eventoSismicoSeleccionado.obtenerDatosClasificacion()
        
    # 36 mostrar datos origen
    def mostrarDatosOrigen(self) -> None:
        self.origen = self.gestor.eventoSismicoSeleccionado.obtenerDatosOrigen()

    # 50 permitir visualizar mapa
    def permitirVisualizarMapa(self,request):
        if request.method == 'POST':
            data = json.loads(request.body)
            opcion = data.get('opcion')
            permitir = self.gestor.tomarRechazoVisualizacion(opcion)
            if opcion == 'No':
                mensaje = "<div class='alert alert-info'>No se quiere visualizar el mapa.</div>"
            elif opcion == 'Si':
                mensaje = "<div class='alert alert-success'>Se permite visualizar el mapa.</div>"
            else:
                mensaje = "<div class='alert alert-danger'>Opción no válida.</div>"
            return JsonResponse({'mensaje': mensaje, 'permitir': permitir})
        return JsonResponse({'mensaje': ''})
            
    # 51 tomar rechazo de visualizar mapa
    def tomarRechazoVisualizacion(self,request): 
        opcion = request.POST.get('opcion')
        permitir_modificar = self.gestor.tomarRechazoVisualizacion(opcion)
        print(f"(: Opción seleccionada: {opcion}")
        # Puedes devolver un JsonResponse o lo que necesites
        return JsonResponse({'permitir_modificar': permitir_modificar})


        
    # 53 permitir modificar datos
    def permitirModificarDatos(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            opcion = data.get('opcion')
            permitir = self.gestor.tomarRechazoModificacion(opcion)
            if opcion == 'No':
                mensaje = "<div class='alert alert-info'>No se quiere modificar datos.</div>"
            elif opcion == 'Si':
                mensaje = "<div class='alert alert-success'>Se permite modificar datos.</div>"
            else:
                mensaje = "<div class='alert alert-danger'>Opción no válida.</div>"
            return JsonResponse({'mensaje': mensaje, 'permitir': permitir})
        return JsonResponse({'mensaje': ''})

    # 54 permitir modificar datos
    def tomarRechazoModificacion(self, request):
        opcion = request.POST.get('opcion')
        permitir_modificar = self.gestor.tomarRechazoModificacion(opcion)
        print(f"(: Opción seleccionada: {opcion}")
        # Puedes devolver un JsonResponse o lo que necesites
        return JsonResponse({'permitir_modificar': permitir_modificar})

    # 56 solicitar accion
    def solicitarAccion(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            opcion = data.get('opcion')
            permitir = self.gestor.tomarAccionRechazarEvento(opcion)

            if opcion == 'No':
                mensaje = "<div class='alert alert-info'>No se quiere rechazar evento.</div>"
            elif opcion == 'Si':
                self.gestor.validarExistenciaDatos()
                self.gestor.validarAccionSeleccionada()
                self.gestor.registrarRechazoEvento()
                mensaje = "<div class='alert alert-success'>Se quiere rechazar evento.</div>"
            else:
                mensaje = "<div class='alert alert-danger'>Opción no válida.</div>"
            return JsonResponse({'mensaje': mensaje, 'permitir': permitir})
        return JsonResponse({'mensaje': ''})

    
    # 57 tomar accion rechazar evento
    def tomarAccionRechazarEvento(self,request):
        opcion = request.POST.get('opcion')
        permitir_modificar = self.gestor.tomarAccionRechazarEvento(opcion)
        print(f"(: Opción seleccionada: {opcion}")
        # Puedes devolver un JsonResponse o lo que necesites
        return JsonResponse({'permitir_modificar': permitir_modificar})





















