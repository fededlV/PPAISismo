from django.db import models
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponse
from ..entities.EventoSismico import EventoSismico
from ..entities.Estado import Estado
from ..entities.Usuario import Usuario
from typing import List
from ..entities.Estado import Estado
from ..boundaries import PantallaRevision


class GestorRevision:
    def __init__(self, eventoSismicoSeleccionado: EventoSismico = None, pantallaRevision:PantallaRevision=None):
        self.eventosSismicosAd = []
        self.eventosSismicos = EventoSismico.objects.all()
        self.eventoSismicoSeleccionado = eventoSismicoSeleccionado
        self.pantallaRevision= pantallaRevision
        self.estados = Estado.objects.all()
        self.accionSeleccionada = None
        self.asLogueado = Usuario.objects.get()  # Usuario logueado

    # 3 Tomar opción seleccionada
    def tomarOpcSeleccionada(self):
        self.buscarEventosSismicos()
        mostrarDatosEventos = self.mostrarDatosEventos()
        self.eventosSismicosAd = self.ordenarPorFechaYHoraOcurrencia(mostrarDatosEventos)
        return self.eventosSismicosAd

    # 4 Buscar eventos sísmicos
    def buscarEventosSismicos(self) -> List[EventoSismico]:
        for evento in self.eventosSismicos:
            if evento.obtenerEventosAd():
                self.eventosSismicosAd.append(evento)
        return self.eventosSismicosAd



    # 8 Mostrar datos de eventos
    def mostrarDatosEventos(self) -> List[dict]: 
        datosEventos = []
        for i in self.eventosSismicosAd:
            datosEventos.append(i.getDatosEventoSismico())
        return datosEventos  

    # 10 Ordenar eventos sismicos
    def ordenarPorFechaYHoraOcurrencia(self, eventos: List[dict]) -> List[dict]:
        return sorted(eventos, key=lambda evento: evento['fechaHoraOcurrencia'], reverse=True)

    # 14 Tomar evento sismico
    def tomarEvento(self, evento_id: int) -> None:
        self.eventoSismicoSeleccionado = next((evento for evento in self.eventosSismicosAd if evento.id == evento_id), None)
        print("eventos", self.eventoSismicosAd)
        print(f"(: Evento sismico seleccionado: {self.eventoSismicoSeleccionado}")
        try:
            estado_bloqueado = self.buscarEstadoBloqueado()
            if estado_bloqueado:
                fechaYHoraActual = self.obtenerFechaHoraActual()
                self.bloquearEvento(fechaYHoraActual, estado_bloqueado)
                self.eventoSismicoSeleccionado.estadoActual = estado_bloqueado
                print(f"(: Evento {evento_id} bloqueado exitosamente")
                return self.mostrarAlcance()
                
        except EventoSismico.DoesNotExist:
            print(f"(: No se encontró el evento con ID {evento_id}")
            
    # 15 Buscar estado bloqueado
    def buscarEstadoBloqueado(self):
        for estado in self.estados:
            if estado.ambitoEventoSismico() and estado.esBloqueado():
                return estado
        return None

    # 18 y 66 Obtener fecha y hora actual
    @staticmethod
    def obtenerFechaHoraActual() -> datetime:
        return timezone.now()
    
    # 19 Bloquear evento
    def bloquearEvento(self, fechaHoraActual: datetime, estado: Estado) -> None:
        eventoSismicoSeleccionado = self.eventoSismicoSeleccionado
        eventoSismicoSeleccionado.bloquear(fechaHoraActual, estado)
          
    # 25 Mostrar alcance
    def mostrarAlcance(self) -> dict:
        return self.eventoSismicoSeleccionado.mostrarAlcance()

    # 29 obtener clasificacion
    def obtenerClasificacion(self) -> dict:
        return self.eventoSismicoSeleccionado.obtenerDatosClasificacion()
    
    # 33 obtener origen
    def obtenerOrigen(self) -> dict:
        return self.eventoSismicoSeleccionado.obtenerDatosOrigen()
    
    # 37 obtener datos de serie y muestra
    def obtenerDatosSerieYMuestra(self) : 
        return self.eventoSismicoSeleccionado.obtenerDatosSerieYmuestra()
    
    # 43 obtener datos estacion
    def obtenerDatosEstacion(self):
        return self.eventoSismicoSeleccionado.obtenerDatosEstacion()
    
    # 44 clasificar por estacion
    def clasificarPorEstacion(self):
        if not self.eventoSismicoSeleccionado:
            raise ValueError("No se ha seleccionado un evento sismico.")
        resultado = {}
        for serie in self.eventoSismicoSeleccionado.serieTemporal.all():
            estacion = getattr(serie.sismografo, 'estacion', None)
            if estacion:
                nombre_estacion = str(estacion)
                if nombre_estacion not in resultado:
                    resultado[nombre_estacion] = []
                resultado[nombre_estacion].append(serie)
        return resultado
    
    # 49 llamar CU 18
    def llamarCU18() -> str:
        return "Llamando CU 18"

    # 52 tomar rechazo de visualizacion del Mapa
    def tomarRechazoVisualizacion(self, opcion):
        return opcion == "Si"
    
    # 55 tomar rechazo de visualizacion del Mapa
    def tomarRechazoModificacion(self, opcion):
        return opcion == "Si"
    
    # 58 tomar accion rechazar evento
    def tomarAccionRechazarEvento(self, opcion):
        self.accionSeleccionada = opcion
        return opcion == "Si"

    # 60. Validar existencia de datods
    def validarExistenciaDatos(self) -> bool: 
        if not self.eventoSismicoSeleccionado:
            raise ValueError("No se ha seleccionado un evento sismico.")
        else: 
            return True
    
    # 61. Validar accion seleccionada
    def validarAccionSeleccionada(self) -> bool: 
        if not self.accionSeleccionada:
            raise ValueError("No se ha seleccionado una acción.")
        else:
            return True
    
    # 62 registrar rechazo del evento sismico 
    def registrarRechazoEvento(self): 
        print("(: Registrando rechazo del evento sismico")
        empleado = self.obtenerEmpleadoLogueado()
        fechaHoraActual = self.obtenerFechaHoraActual()
        estadosRechazado = self.buscarEstadoRechazado()
        self.registrarRevision(estadosRechazado,fechaHoraActual,self.asLogueado.empleado)
        self.finCU()
        print()
        print(estadosRechazado)
        print(empleado)
        print(fechaHoraActual)
        print(estadosRechazado)
        return None

    # 63 Obtener empleado logueado
    def obtenerEmpleadoLogueado(self): 
        return self.asLogueado.getAsLogueado()
    
    # 67 Buscar estados rechazados
    def buscarEstadoRechazado(self) -> List[Estado]:
        for estado in self.estados:
            if estado.ambitoEventoSismico() and estado.esRechazado():
                return estado
        return None
                
    # 70 Registrar revision
    def registrarRevision(self, estado: Estado, fechaHoraActual: datetime,empleado) -> None:
        self.eventoSismicoSeleccionado.registrarRevision(estado=estado, fechaHoraActual=fechaHoraActual, empleado=empleado)
        
    # 76 Fin de CU
    def finCU(self):
        return "Fin de CU"
