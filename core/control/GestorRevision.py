from datetime import datetime
from django.utils import timezone
from ..entities.EventoSismico import EventoSismico
from ..entities.Estado import Estado
from ..entities.Usuario import Usuario
from typing import List
from ..entities.Estado import Estado
from ..boundaries import PantallaRevision
from ..entities.Sesion import Sesion


class GestorRevision:
    def __init__(self, eventoSismicoSeleccionado: EventoSismico = None, pantallaRevision:PantallaRevision=None):
        self.eventosSismicosAd = [] # Lista de eventos sismicos auto detectados (Son objetos) 
        self.eventosSismicos = EventoSismico.objects.all()
        self.eventoSismicoSeleccionado = eventoSismicoSeleccionado
        self.pantallaRevision= pantallaRevision
        #self.estados = Estado.objects.all()
        self.fechaHoraActual = self.obtenerFechaHoraActual()
        self.accionSeleccionada = None
        self.asLogueado = Usuario.objects.get()  # Usuario logueado
        self.sesion = Sesion(usuario=Usuario.objects.get(), fecha_inicio=timezone.now(), fecha_fin=None)  # Sesión del usuario

    # 3 Tomar opción seleccionada
    def tomarOpcSeleccionada(self):
        self.buscarEventosSismicos()
        self.eventosSismicosAd = self.ordenarPorFechaYHoraOcurrencia(self.eventosSismicosAd)
        mostrarDatosEventos = self.mostrarDatosEventos()
        print(f"(: Eventos sismicos encontrados: {self.eventosSismicosAd}")
        return mostrarDatosEventos

    # 4 Buscar eventos sísmicos
    def buscarEventosSismicos(self) -> List[EventoSismico]:
        print("Todos los eventos sismicos: ", self.eventosSismicos)
        eventosAd =[]
        for evento in self.eventosSismicos:
            print(f"Evento {evento.id}: obtenerEventosAd() = {evento.obtenerEventosAd()}")
            if evento.obtenerEventosAd():
                eventosAd.append(evento)
        print("Eventos AD encontrados: ", eventosAd)
        self.eventosSismicosAd = eventosAd



    # 8 Mostrar datos de eventos
    def mostrarDatosEventos(self) -> List[dict]: 
        datosEventos = []
        print(self.eventosSismicosAd)
        for i in self.eventosSismicosAd:
            datosEventos.append(i.getDatosEventoSismico())
        return datosEventos  

    # 10 Ordenar eventos sismicos
    def ordenarPorFechaYHoraOcurrencia(self, eventos: List[EventoSismico]) -> List[EventoSismico]:
        return sorted(eventos, key=lambda evento: evento.fechaHoraOcurrencia, reverse=True)

    # 14 Tomar evento sismico
    def tomarEvento(self, evento_id: int) -> None:
        print("(: === INICIANDO tomarEvento ===")
        print(f"(: Eventos disponibles: {len(self.eventosSismicosAd)}")
        print(f"(: Evento ID recibido: {evento_id}")
        
        try:
            evento_id = int(evento_id)
        except (TypeError, ValueError):
            print("(: ❌ ID de evento inválido:", evento_id)
            self.eventoSismicoSeleccionado = None
            return None
        
        # Buscar el evento en la lista
        self.eventoSismicoSeleccionado = next(
            (evento for evento in self.eventosSismicosAd if evento.id == evento_id), 
            None
        )
        
        if self.eventoSismicoSeleccionado:
            print(f"(: ✓ Evento seleccionado: {self.eventoSismicoSeleccionado.id}")
            print(f"(: Estado actual ANTES del bloqueo: {self.eventoSismicoSeleccionado.estadoActual.nombreEstado}")
            
            # 19 - Bloquear el evento (¡ESTO ES CLAVE!)
            print("(: Llamando a bloquearEvento()...")
            self.bloquearEvento()
            
            # Recargar el evento desde la BD para ver el cambio
            self.eventoSismicoSeleccionado.refresh_from_db()
            print(f"(: Estado actual DESPUÉS del bloqueo: {self.eventoSismicoSeleccionado.estadoActual.nombreEstado}")
            print("(: === tomarEvento COMPLETADO ===\n")
        else:
            print(f"(: ❌ No se encontró el evento con ID {evento_id}")
            
    # 15 Buscar estado bloqueado (ya no es necesario con polimorfismo)
    # El estado se maneja automáticamente en el patrón State

    # 18 y 66 Obtener fecha y hora actual
    @staticmethod
    def obtenerFechaHoraActual() -> datetime:
        return timezone.now()
    
    # 19 Bloquear evento
    def bloquearEvento(self) -> None:
        print("(: --- Iniciando bloquearEvento() ---")
        print(f"(: Evento a bloquear: ID={self.eventoSismicoSeleccionado.id}")
        print(f"(: Tipo del estadoActual: {type(self.eventoSismicoSeleccionado.estadoActual).__name__}")
        
        # Delegamos al evento que a su vez delega al estado (Patrón State)
        self.eventoSismicoSeleccionado.bloquear(self.fechaHoraActual)
        
        print("(: --- bloquearEvento() COMPLETADO ---\n")
          
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
        return self.sesion.getUsuarioLogueado()
    
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
