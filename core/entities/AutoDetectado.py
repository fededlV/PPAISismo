from typing import List
from django.db import models
from .Estado import Estado    
from .CambioEstado import CambioEstado
from datetime import datetime


class AutoDetectado(Estado):
    """
    Estado concreto AutoDetectado - Persiste en BD
    Sobreescribe el método bloquear() con lógica específica
    """
    
    class Meta:
        app_label = 'core'
        # No es abstracto, se creará una tabla en la BD
    
    def __str__(self):
        return f"Estado AutoDetectado (ID: {self.id})"

    def buscarCambioEstadoActual(self, ce: List[CambioEstado]) -> CambioEstado:
        """
        Busca el cambio de estado actual en la lista de cambios de estado.
        
        Parámetros:
        - ce: lista de CambioEstado del evento
        
        Retorna:
        - El CambioEstado actual (con fechaHoraFin = None) o None si no existe
        """
        return next((cambio for cambio in ce if cambio.esActual()), None)

    def bloquear(self, fechaHora: datetime, ce: List[CambioEstado], e) -> None:
        """
        Implementación concreta del bloqueo para el estado AutoDetectado.
        
        Parámetros:
        - fechaHora: fecha y hora actual del bloqueo (viene del GestorRevision)
        - ce: lista de CambioEstado del evento (viene del EventoSismico)
        - e: referencia al EventoSismico que se está bloqueando (viene del EventoSismico)
        """
        print(f"AutoDetectado: Bloqueando evento {e.id} en {fechaHora}")
        
        # 1. Buscar el cambio de estado actual en la lista recibida
        cambioEstadoActual = self.buscarCambioEstadoActual(ce)
        
        if cambioEstadoActual:
            # 2. Finalizar el cambio de estado actual
            cambioEstadoActual.setFechaHoraFin(fechaHora)
            cambioEstadoActual.save()
            print(f"   - Cambio de estado actual finalizado: {cambioEstadoActual}")
        
        # 3. Buscar o crear el estado Bloqueado usando la clase correcta
        from .Bloqueado import Bloqueado
        estado_bloqueado = Bloqueado.objects.filter(
            nombreEstado="Bloqueado",
            ambito="EventoSismico"
        ).first()
        
        if not estado_bloqueado:
            estado_bloqueado = Bloqueado.objects.create(
                nombreEstado="Bloqueado",
                ambito="EventoSismico"
            )
            print(f"   - Estado Bloqueado creado")
        else:
            print(f"   - Estado Bloqueado encontrado: {estado_bloqueado.id}")
        
        # 4. Crear nuevo cambio de estado a Bloqueado
        nuevo_cambio_estado = e.crearCambioEstado(
            estado=estado_bloqueado, 
            fechaHora=fechaHora
        )
        print(f"   - Nuevo cambio de estado creado: {nuevo_cambio_estado}")
        
        # 5. Actualizar el estado actual del evento
        e.setEstado(estado_bloqueado)
        e.setCambioEstado(nuevo_cambio_estado)
        e.save()
        print(f"   - Evento bloqueado exitosamente. Nuevo estado: {e.estadoActual}")

    