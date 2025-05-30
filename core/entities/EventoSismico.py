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

    @classmethod
    def obtenerEventosAd(cls):
        """
        Obtiene los eventos sismicos activos en la base de datos.
        :return: Lista de eventos sismicos activos.
        """
        eventosSismicos = EventoSismico.objects.all()
        ambitoEstadoSismico = []
        for evento in eventosSismicos:
            a = evento.estadoActual.esAmbitoEventoSismico()
            b = evento.estadoActual.esAutoDetectado()
            if a and b:
                ambitoEstadoSismico.append(evento)
        return ambitoEstadoSismico

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

    def crearCambioEstado(self, fechaHora, estado=None, empleado=None):
        """
        Crea un nuevo cambio de estado para el evento sismico.
        :return: Nuevo cambio de estado creado.
        """
        if estado:
            cambioEstadoActual = next((ce for ce in self.cambioEstado.all() if ce.esActual()), None)
            if cambioEstadoActual:
                cambioEstadoActual.setFechaHoraFin(fechaHora)


        nuevoCambioEstado = CambioEstado(
            evento=self,
            estado=estado,
            empleado=empleado,
            fechaHoraInicio=fechaHora
        )
        nuevoCambioEstado.save()
        self.cambioEstado.add(nuevoCambioEstado)
        return nuevoCambioEstado
    
    def bloquear(self, fechaHora):
        cambioEstadoActual = next((ce for ce in self.cambioEstado.all() if ce.esActual()), None)
        if cambioEstadoActual:
            cambioEstadoActual.setFechaHoraFin(fechaHora)
            self.crearCambioEstado(self)
    
    def get_fechaHoraFin(self):
        return self.fechaHoraFin

    def set_fechaHoraFin(self, value):
        self.fechaHoraFin = value

    def get_fechaHoraOcurrencia(self):
        return self.fechaHoraOcurrencia

    def set_fechaHoraOcurrencia(self, value):
        self.fechaHoraOcurrencia = value

    def get_latitudEpicentro(self):
        return self.latitudEpicentro

    def set_latitudEpicentro(self, value):
        self.latitudEpicentro = value

    def get_latitudHipocentro(self):
        return self.latitudHipocentro

    def set_latitudHipocentro(self, value):
        self.latitudHipocentro = value

    def get_longitudEpicentro(self):
        return self.longitudEpicentro

    def set_longitudEpicentro(self, value):
        self.longitudEpicentro = value

    def get_longitudHipocentro(self):
        return self.longitudHipocentro

    def set_longitudHipocentro(self, value):
        self.longitudHipocentro = value

    def get_valorMagnitud(self):
        return self.valorMagnitud

    def set_valorMagnitud(self, value):
        self.valorMagnitud = value

    def get_estadoActual(self):
        return self.estadoActual

    def set_estadoActual(self, value):
        self.estadoActual = value

    def get_alcanceSismo(self):
        return self.alcanceSismo

    def set_alcanceSismo(self, value):
        self.alcanceSismo = value

    def get_clasificacion(self):
        return self.clasificacion

    def set_clasificacion(self, value):
        self.clasificacion = value

    def get_origenGeneracion(self):
        return self.origenGeneracion

    def set_origenGeneracion(self, value):
        self.origenGeneracion = value

    def get_serieTemporal(self):
        return self.serieTemporal.all()

    def set_serieTemporal(self, series):
        self.serieTemporal.set(series)

    def get_cambioEstado(self):
        return self.cambioEstado.all()

    def set_cambioEstado(self, cambios):
        self.cambioEstado.set(cambios)

    def get_analistaSuperior(self):
        return self.analistaSuperior

    def set_analistaSuperior(self, value):
        self.analistaSuperior = value