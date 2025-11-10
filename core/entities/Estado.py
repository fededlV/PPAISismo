from django.db import models
from polymorphic.models import PolymorphicModel
from datetime import datetime

class Estado(PolymorphicModel):
    ambito = models.CharField(max_length=100)
    nombreEstado = models.CharField(max_length=100)

    def __str__(self):
        return f"Alcance {self.nombreEstado}"
    
    def new(self):
        print(f"Creando nuevo estado: {self.nombreEstado} con ambito: {self.ambito}")
        return self

    def pendienteRevision(self):
        print(f"Estado {self.nombreEstado} está pendiente de revisión.")
    
    def porRevisar(self):
        print(f"Estado {self.nombreEstado} por revisar.")
    
    def bloquear(self, fechaHora: datetime, ce, e):
        """
        Implementación por defecto del método bloquear.
        Las subclases concretas (AutoDetectado, PendienteRevision, etc.) 
        pueden sobreescribir este método para implementar su lógica específica.
        
        Parámetros:
        - fechaHora: fecha y hora actual del bloqueo
        - ce: lista de CambioEstado del evento
        - e: referencia al EventoSismico que se está bloqueando
        """
        print(f"Estado base: Bloqueando desde estado {self.nombreEstado} en {fechaHora}.")
        # Implementación por defecto (puede no hacer nada o lanzar excepción)

    def sinRevisar(self):
        print(f"Estado {self.nombreEstado} sin revisar.")
    
    def rechazar(self):
        print(f"Estado {self.nombreEstado} rechazado.")
    
    def confirmar(self):
        print(f"Estado {self.nombreEstado} confirmado.")

    def derivar(self):
        print(f"Estado {self.nombreEstado} derivado.")
    
    def porCerrar(self):
        print(f"Estado {self.nombreEstado} por cerrar.")
    
    def cerrar(self):
        print(f"Estado {self.nombreEstado} cerrado.")
    
    def adquirirDatos(self):
        print(f"Adquiriendo datos para el estado {self.nombreEstado}.")
    
    # 6, 16 Ambito eventos sismicos
    def ambitoEventoSismico(self):
        return self.ambito == "EventoSismico"

    # 7 Es auto detectado
    def esAutoDetectado(self):
        print(self.nombreEstado)
        return self.nombreEstado == "AutoDetectado"

    # 17 Es bloqueado
    def esBloqueado(self):
        return self.nombreEstado == "Bloqueado"

    def esRechazado(self):
        return self.nombreEstado == "Rechazado"
    
    def esPendienteRevision(self):
        return self.nombreEstado == "PendienteRevision"
    
    def getAmbito(self):
        return self.ambito

    def getNombreEstado(self):
        return self.nombreEstado

    class Meta:
        app_label = 'core'
        # abstract = True  # Comentado para permitir consultas directas a Estado

