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


class GestorRevision:
    def __init__(self, eventoSismicoSeleccionado: EventoSismico = None):
        self.eventosSismicosAd = EventoSismico.objects.all()
        self.eventoSismicoSeleccionado = eventoSismicoSeleccionado

    # 3 Tomar opción seleccionada
    def tomarOpcSeleccionada(self):
        self.buscarEventosSismicos()
        mostrarDatosEventos = self.mostrarDatosEventos()
        self.eventosSismicosAd = self.ordenarPorFechaYHoraOcurrencia(mostrarDatosEventos)
        return self.eventosSismicosAd

    # 4 Buscar eventos sísmicos
    def buscarEventosSismicos(self) -> List[EventoSismico]:
        self.eventosSismicosAd = EventoSismico.obtenerEventosAd(self)

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
        self.eventoSismicoSeleccionado = self.eventosSismicosAd.get(id=evento_id)
        try:
            estado_bloqueado = self.buscarEstadoBloqueado()
            if estado_bloqueado:
                fechaYHoraActual = self.obtenerFechaHoraActual()
                self.bloquearEvento(fechaYHoraActual, estado_bloqueado)
                print(f"(: Evento {evento_id} bloqueado exitosamente")
                return self.mostrarAlcance()
                
        except EventoSismico.DoesNotExist:
            print(f"(: No se encontró el evento con ID {evento_id}")
            
    # 15 Buscar estado bloqueado
    def buscarEstadoBloqueado(self):
        estados = Estado.objects.all()
        for estado in estados:
            if estado.ambitoEventoSismico() and estado.esBloqueado():
                return estado
        return None

    # 18 Obtener fecha y hora actual
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
    
    
    
    @staticmethod
    def obtenerDatosEstacion(evento: EventoSismico) -> dict:
        return evento.obtenerDatosEstacion()
    


    @staticmethod
    def obtenerDatosEstacion(): pass
    
    @staticmethod
    def clasificarPorEstacion() : pass
    
    @staticmethod
    def llamarCU18() -> str:
        return "Llamando CU 18"

    @staticmethod
    def tomarRechazoVisualizacion(opcion: str) -> bool:
        """ 
        Procesa el rechazo de visualización de un evento sismico.
        :param opcion: Opción seleccionada por el usuario.
        :return: True si la opción Visualizar, False en caso contrario.
        """
        if opcion == "Rechazar":
            print("(: Opción seleccionada: Rechazar")
            return True
        return False
    
    @staticmethod
    def tomarRechazoModificacion(opcion: str, valor_rechazo: str = "Si") -> bool:
        """
        Procesa el rechazo de modificación de un evento sismico.
        :param opcion: Opción seleccionada por el usuario.
        :param valor_rechazo: Valor que representa el rechazo (por defecto "Si").
        :return: True si la opción es igual a valor_rechazo, False en caso contrario.
        """
        if opcion == valor_rechazo:
            print(f"(: Opción seleccionada: {valor_rechazo}")
            return True
        return False
    
    @staticmethod
    def tomarAccionRechazarEvento(self, opcion: str) -> bool:
        """
        Procesa la acción de rechazar un evento sismico.
        :param opcion: Opción seleccionada por el usuario.
        :return: True si la opción es "Rechazar", False en caso contrario.
        """
        if opcion == "Rechazar":
            print("(: Opción seleccionada: Rechazar")
            self.accionSeleccionada = opcion
            return True
        return False

    @staticmethod
    def validarExistenciaDatos(self): 
        if not self.eventoSismicoSeleccionado:
            raise ValueError("No se ha seleccionado un evento sismico.")
        else: 
            return True
    
    @staticmethod
    def validarAccionSeleccionada(self): 
        if not self.accionSeleccionada:
            raise ValueError("No se ha seleccionado una acción.")
        else:
            return True
    
    @staticmethod
    def registrarRechazoEvento(self): 
        print("(: Registrando rechazo del evento sismico")
        #Aca no se que mas podriamos hacer en este metodo, ya que solamente seria como un disparador de todo, el cual ese todo comenzaria con el self de obtenerEmpleadoLogueado()
    
    @staticmethod
    def obtenerEmpleadoLogueado(usuario: Usuario): 
        asLogueado = usuario.getAsLogueado()
        return usuario.getAsLogueado()
    
    
    # @staticmethod
    # def buscarEstadoRechazado(estados: list[Estado]) -> list[Estado]:
    #     """
    #     Busca los estados rechazados en una lista de estados.
    #     :param estados: Lista de objetos Estado.
    #     :return: Lista de estados que son de ámbito EventoSismico y están rechazados.
    #     """
    #     estadosRechazados = []
    #     for estado in estados:
    #         if estado.ambitoEventoSismico() and estado.esRechazado():
    #             estadosRechazados.append(estado)
    #     return estadosRechazados
                
    @staticmethod
    def registrarRevision(self):
        self.eventoSismicoSeleccionado.registrarRevision("rechazado", self.fechaHoraActual, self.asLogueado)
        
    @staticmethod
    def finCU() -> str:
        return "Fin de CU"
