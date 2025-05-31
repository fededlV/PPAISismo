from django.db import models
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponse
from ..entities.EventoSismico import EventoSismico
from ..entities.Estado import Estado
from ..entities.Usuario import Usuario
from typing import List


class GestorRevision:
    def __init__(self):
        self.eventos = EventoSismico.objects.all()  # Obtiene todos los eventos sismicos
        self.estados = Estado.objects.all()
        self.eventosSismicosAd = []
        self.eventoSismicoSeleccionado = None
        self.alcanceEvento = None
        self.clasificacionEvento = None
        self.origenEvento = None
        self.valoresVelocidadDeOnda = []
        self.valoresFrecuenciaDeOnda = []
        self.valoresLongitud = []
        self.fechaHoraActual = None
        self.asLogueado = None
        self.accionSeleccionada = None


    """ @staticmethod
    def tomarOpcSeleccionada(opcion: str) -> HttpResponse:
        Toma la opcion seleccionada por el usuario.
        :param opcion: Opcion seleccionada.
        :return: HttpResponse con la opcion seleccionada.
        
        return HttpResponse(f"Opcion seleccionada: {opcion}") """
    
    #3. Listo
    def tomarOpcSeleccionada(self): 
        eventos = self.eventos  # Obtiene todos los eventos sismicos
        self.buscarEventosSismicos()
        mostraDatos = self.mostrarDatosEventos()
        self.eventosSismicosAd = self.ordenarEventos()
        return self.eventosSismicosAd
    
    #4. Listo | Funcion para buscar los eventos sismicos auto detectados. 
    def buscarEventosSismicos(self):
        eventos = self.eventos #Agarra el atributo que contiene los eventos 
        eventosAD = [] #Lista de eventos sismicos auto detectados
        for evento in eventos:
            if evento.obtenerEventosAD():
                eventosAD.append(evento)
        self.eventosSismicosAd = eventosAD

    #8. Listo
    def mostrarDatosEventos(self):
        eventosAD = self.eventosSismicosAd
        eventoDatos = []
        for evento in eventosAD: 
            fechaHoraFin = evento.getFechaHoraFin()
            fechaHoraOcurrencia = evento.getFechaHoraOcurrencia()
            latitudEpicentro = evento.getLatitudEpicentro()
            latitudHipocentro = evento.getLatitudHipocentro()
            longitudEpicentro = evento.getLongitudEpicentro()
            longitudHipocentro = evento.getLongitudHipocentro()
            valorMagnitud = evento.getValorMagnitud()
            eventoData = {
                    'fechaHoraFin': fechaHoraFin,
                    'fechaHoraOcurrencia': fechaHoraOcurrencia,
                    'latitudEpicentro': latitudEpicentro,
                    'latitudHipocentro': latitudHipocentro,
                    'longitudEpicentro': longitudEpicentro,
                    'longitudHipocentro': longitudHipocentro,
                    'valorMagnitud': valorMagnitud
            }
            eventoDatos.append(eventoData)
        self.eventosSismicosAd = eventoDatos
        
            
        
    #10. Listo
    def ordenarEventos(self):
        """
        Ordena los eventos sismicos por fecha y hora de ocurrencia.
        :param eventos: Lista de eventos sismicos.
        :return: Lista de eventos sismicos ordenados.
        """
        eventosAD = self.eventosSismicosAd
        eventosAD.sort(key=lambda x: x["fechaHoraOcurrencia"], reverse=True)

        return eventosAD
    
    #14. Listo | obtiene la fecha, latitud y longitud 
    def tomarEvento(self, fecha, lat, lon):
        """
        Toma un evento sismico por su ID.
        :param evento_id: ID del evento sismico.
        :return: HttpResponse con el evento sismico.
        """
        print("Iniciada la busqueda del evento sismico")
        print(self.eventosSismicosAd)
        print(f"Fecha: {fecha}, Latitud: {lat}, Longitud: {lon}")
        for evento in self.eventosSismicosAd: #Esta busqueda mejorarla. 
            if (str(evento["fechaHoraOcurrencia"]) == fecha and
                str(evento["latitudEpicentro"]) == lat and
                str(evento["longitudEpicentro"]) == lon):
                self.eventoSismicoSeleccionado = evento 
                print("Evento sismico encontrado")
                self.buscarEstadoBloqueado()
                self.obtenerFechaHoraActual()
                self.bloquearEvento()
                print("Secuencia ejecutada correctamente")
                return self.eventoSismicoSeleccionado
        print("No se encontró el evento sismico con los datos proporcionados")
        return None
        
    #15. 
    def buscarEstadoBloqueado(self):
        """
        Busca el estado bloqueado de un evento sismico.
        :param evento: Evento sismico.
        :return: Estado bloqueado del evento sismico.
        """
        print("(: Buscando estado bloqueado del evento sismico")
        for estado_obj in self.estados:
            if estado_obj.esAmbitoEventoSismico() and estado_obj.esBloqueado():
                print("Se encontro un estado bloqueado") 
                return estado_obj
        return None

    #18. 
    def obtenerFechaYHoraActual(self):
        """
        Obtiene la fecha y hora actual.
        :return: Fecha y hora actual.
        """
        print("(: Obteniendo fecha y hora actual")
        self.fechaHoraActual = timezone.now()
        return self.fechaHoraActual
    

    def bloquearEvento(self):
        """
        Cambia el estado de un evento sismico a bloqueado.
        :param eventoBloqueado: Evento sismico a bloquear.
        :param fechaYHoraActual: Fecha y hora actual.
        """
        return self.eventoSismicoSeleccionado.bloquear(self.fechaHoraActual)
        
        
          
    
    """ @staticmethod
    def tomarEvento(evento_id: int) -> None:
        
        Cambia el estado de un evento sismico a bloqueado.
        :param evento_id: ID del evento sismico a bloquear.
        
        try:
            evento = EventoSismico.objects.get(id=evento_id)
            estado_bloqueado = GestorRevision.buscarEstadoBloqueado(evento)
            if estado_bloqueado:
                fechaYHoraActual = GestorRevision.obtenerFechaYHoraActual()
                evento.bloquear(fechaYHoraActual)
                
                print(f"(: Evento {evento_id} bloqueado exitosamente")
            else:
                print("(: No se encontró un estado bloqueado válido")

            
        except EventoSismico.DoesNotExist:
            print(f"(: No se encontró el evento con ID {evento_id}") """

    @staticmethod
    def mostrarAlcance(evento: EventoSismico) -> dict:
        """
        Muestra el alcance del evento sismico.
        :param evento: Evento sismico.
        :return: Diccionario con los datos del alcance del evento sismico.
        """
        return evento.alcance.getDatosAlcance()

    # cambiar el nombre a obtenerClasificacion()
    @staticmethod
    def obtenerClasificacion(evento: EventoSismico) -> dict:
        """
        Obtiene los datos de la clasificación del evento sismico.
        :param evento: Evento sismico.
        :return: Diccionario con los datos de la clasificación del evento sismico.
        """
        return evento.obtenerDatosClasificacion()
    
    @staticmethod
    def obtenerOrigen(evento: EventoSismico) -> dict:
        return evento.obtenerDatosOrigen()
    
    @staticmethod
    def obtenerDatosEstacion(evento: EventoSismico) -> dict:
        return evento.obtenerDatosEstacion()
    
    @staticmethod
    def obtenerDatosSerieYMuestra(evento: EventoSismico) : 
        return evento.obtenerDatosSerieYMuestra()

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
    
    @staticmethod
    def obtenerFechaHoraActual() -> datetime:
        return timezone.now()
    
    @staticmethod
    def buscarEstadoRechazado(estados: list[Estado]) -> list[Estado]:
        """
        Busca los estados rechazados en una lista de estados.
        :param estados: Lista de objetos Estado.
        :return: Lista de estados que son de ámbito EventoSismico y están rechazados.
        """
        estadosRechazados = []
        for estado in estados:
            if estado.esAmbitoEventoSismico() and estado.esRechazado():
                estadosRechazados.append(estado)
        return estadosRechazados
                
    @staticmethod
    def registrarRevision(self):
        self.eventoSismicoSeleccionado.registrarRevision("rechazado", self.fechaHoraActual, self.asLogueado)
        
    @staticmethod
    def finCU() -> str:
        return "Fin de CU"
