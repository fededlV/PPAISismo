from django.db import models
from .Estado import Estado
from typing import List
from .AlcanceSismo import AlcanceSismo
from .ClasificacionSismo import ClasificacionSismo
from .OrigenDeGeneracion import OrigenDeGeneracion
from .SerieTemporal import SerieTemporal
from .CambioEstado import CambioEstado
from .Empleado import Empleado


class EventoSismico(models.Model):
    fechaHoraFin = models.DateTimeField()
    fechaHoraOcurrencia = models.DateTimeField()
    latitudEpicentro = models.FloatField()
    latitudHipocentro = models.FloatField()
    longitudEpicentro = models.FloatField()
    longitudHipocentro = models.FloatField()
    valorMagnitud = models.FloatField()

    estadoActual = models.ForeignKey(Estado, on_delete=models.PROTECT, related_name='eventos_actuales')
    alcanceSismo = models.ForeignKey(AlcanceSismo,on_delete=models.PROTECT, related_name='eventos_alcance')
    clasificacion = models.ForeignKey(ClasificacionSismo,on_delete=models.PROTECT,related_name='eventos_clasificados')
    origenGeneracion = models.ForeignKey(OrigenDeGeneracion,on_delete=models.PROTECT,related_name='eventos_origen')
    serieTemporal = models.ManyToManyField(SerieTemporal, related_name='eventos')
    #Agregue esto para poder representar la relacion del evento sismico con los cambios de estado. -> FEDE
    cambioEstado = models.ManyToManyField(CambioEstado, related_name='eventos_cambios_estado')
    analistaSuperior = models.ForeignKey(Empleado, on_delete=models.PROTECT, related_name='eventos_analista_superior', null=True, blank=True)
    
    class Meta:
        app_label = 'core'

    #5. Listo
    def obtenerEventosAD(self):
        """
        Obtiene los eventos sismicos activos en la base de datos.
        :return: Lista de eventos sismicos activos.
        """
        return self.estadoActual.ambitoEventosSismico() and self.estadoActual.esAutoDetectado() 

    def bloquear(self, fechaHora):
        cambioEstadoActual = next((ce for ce in self.cambioEstado.all() if ce.esActual()), None) #Esta línea busca el primer elemento de la colección self.cambioEstado.all() que cumpla con la condición ce.esActual(). Si no encuentra ninguno, devuelve None.
        if cambioEstadoActual:
            cambioEstadoActual.setFechaHoraFin(fechaHora)
            self.crearCambioEstado(self) 
        print("Se finalizo el estado actual")

    def crearCambioEstado(self, fechaHora, estado=None, empleado=None):
        """
        Crea un nuevo cambio de estado para el evento sismico.
        :return: Nuevo cambio de estado creado.
        """


        nuevoCambioEstado = CambioEstado(
            evento=self,
            estado=estado,
            empleado=empleado,
            fechaHoraInicio=fechaHora
        )
        nuevoCambioEstado.save()
        self.cambioEstado.add(nuevoCambioEstado)
        print("Se creo un nuevo cambio de estado")
        return nuevoCambioEstado

    def mostrarAlcance(self):
        """
        Muestra el alcance del evento sismico.
        :return: Alcance del evento sismico.
        """
        return self.alcance.getDatosAlcance()
    
    def obtenerDatosClasificacion(self):
        """
        Obtiene los datos de la clasificación del evento sismico.
        :return: Diccionario con los datos de la clasificación.
        """
        return self.clasificacion.getDatosClasificacion()
    
    def obtenerDatosOrigen(self):
        return self.origen.getDatosOrigen()
    
    def obtenerDatosSerieYmuestra(self):
        return [serie.obtenerDatosMuestras() for serie in self.serieTemporal.all()]

    def obtenerDatosEstacion(self):
        return [serie.obtenerDatosEstacion() for serie in self.serieTemporal.all()]

    def registrarRevision(self, fechaHoraActual, estado, empleado):
        """
        Registra la revisión del evento cambiando el estado actual y creando uno nuevo.
        """
        self.crearCambioEstado(estado, fechaHoraActual, empleado)

    
    
    
    
    #9. Listo | Todos estos para abajo representan el getDatosEventoSismico()
    def getFechaHoraFin(self):
        return self.fechaHoraFin

    def setFechaHoraFin(self, value):
        self.fechaHoraFin = value

    def getFechaHoraOcurrencia(self):
        return self.fechaHoraOcurrencia

    def setFechaHoraOcurrencia(self, value):
        self.fechaHoraOcurrencia = value

    def getLatitudEpicentro(self):
        return self.latitudEpicentro

    def setLatitudEpicentro(self, value):
        self.latitudEpicentro = value

    def getLatitudHipocentro(self):
        return self.latitudHipocentro

    def setLatitudHipocentro(self, value):
        self.latitudHipocentro = value

    def getLongitudEpicentro(self):
        return self.longitudEpicentro

    def setLongitudEpicentro(self, value):
        self.longitudEpicentro = value

    def getLongitudHipocentro(self):
        return self.longitudHipocentro

    def setLongitudHipocentro(self, value):
        self.longitudHipocentro = value

    def getValorMagnitud(self):
        return self.valorMagnitud

    def setValorMagnitud(self, value):
        self.valorMagnitud = value

    def getEstadoActual(self):
        return self.estadoActual

    def setEstadoActual(self, value):
        self.estadoActual = value

    def getAlcanceSismo(self):
        return self.alcanceSismo

    def setAlcanceSismo(self, value):
        self.alcanceSismo = value

    def getClasificacion(self):
        return self.clasificacion

    def setClasificacion(self, value):
        self.clasificacion = value

    def getOerigenGeneracion(self):
        return self.origenGeneracion

    def setOrigenGeneracion(self, value):
        self.origenGeneracion = value

    def getSerieTemporal(self):
        return self.serieTemporal.all()

    def setSerieTemporal(self, series):
        self.serieTemporal.set(series)

    def getCambioEstado(self):
        return self.cambioEstado.all()

    def setCambioEstado(self, cambios):
        self.cambioEstado.set(cambios)

    def getAnalistaSuperior(self):
        return self.analistaSuperior

    def setAnalistaSuperior(self, value):
        self.analistaSuperior = value