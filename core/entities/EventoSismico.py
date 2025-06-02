from django.db import models
from .Estado import Estado
from typing import List
from .AlcanceSismico import AlcanceSismico
from .ClasificacionSismo import ClasificacionSismo
from .OrigenDeGeneracion import OrigenDeGeneracion
from .SerieTemporal import SerieTemporal
from .CambioEstado import CambioEstado
from .Empleado import Empleado
from datetime import datetime


class EventoSismico(models.Model):
    fechaHoraFin = models.DateTimeField()
    fechaHoraOcurrencia = models.DateTimeField()
    latitudEpicentro = models.FloatField()
    latitudHipocentro = models.FloatField()
    longitudEpicentro = models.FloatField()
    longitudHipocentro = models.FloatField()
    valorMagnitud = models.FloatField()

    estadoActual = models.ForeignKey(Estado, on_delete=models.PROTECT, related_name='eventos_actuales')
    alcanceSismico = models.ForeignKey(AlcanceSismico,on_delete=models.PROTECT, related_name='eventos_alcance')
    clasificacion = models.ForeignKey(ClasificacionSismo,on_delete=models.PROTECT,related_name='eventos_clasificados')
    origenGeneracion = models.ForeignKey(OrigenDeGeneracion,on_delete=models.PROTECT,related_name='eventos_origen')
    serieTemporal = models.ManyToManyField(SerieTemporal, related_name='eventos')
    #Agregue esto para poder representar la relacion del evento sismico con los cambios de estado. -> FEDE
    cambioEstado = models.ManyToManyField(CambioEstado, related_name='eventos_cambios_estado')
    analistaSuperior = models.ForeignKey(Empleado, on_delete=models.PROTECT, related_name='eventos_analista_superior', null=True, blank=True)
    
    def __str__(self):
        return f"Evento {self.id} - {self.estadoActual}"
    
    class Meta:
        app_label = 'core'

    # 5 Obtener eventos sismicos
    def obtenerEventosAd(self):
        eventosSismicos = EventoSismico.objects.all()
        ambitoEstadoSismico = []
        for evento in eventosSismicos:
            a = evento.estadoActual.ambitoEventoSismico()
            b = evento.estadoActual.esAutoDetectado()
            if a and b:
                ambitoEstadoSismico.append(evento)
        return ambitoEstadoSismico 
    
    # 9 Obtener datos del evento sismico
    def getDatosEventoSismico(self):
        return {
            'id': self.id,
            'fechaHoraOcurrencia': self.fechaHoraOcurrencia,
            'fechaHoraFin': self.fechaHoraFin,
            'latitudEpicentro': self.latitudEpicentro,
            'latitudHipocentro': self.latitudHipocentro,
            'longitudEpicentro': self.longitudEpicentro,
            'longitudHipocentro': self.longitudHipocentro,
            'valorMagnitud': self.valorMagnitud,
            'estadoActual': self.estadoActual.nombreEstado,
            'ambitoEstado': self.estadoActual.ambito,  # <-- agrega esta línea
            'alcanceSismico': self.alcanceSismico.getDatosAlcance(),
            'clasificacion': self.clasificacion.getDatosClasificacion(),
            'origenGeneracion': self.origenGeneracion.getDatosOrigen(),
            'serieTemporal': self.serieTemporal,
            'cambioEstado': self.cambioEstado,
            'analistaSuperior': self.analistaSuperior
        }
    
    # 74
    def crearCambioEstado(self, estado: Estado, fechaHora: datetime, empleado=None):
        cambioEstadoActual = next((ce for ce in self.cambioEstado.all() if ce.esActual()), None)
        if cambioEstadoActual:

            cambioEstadoActual.setFechaHoraFin(fechaHora)
            cambioEstadoActual.save()
        nuevoCambioEstado = CambioEstado(
            evento=self,
            estado=estado,
            empleado=empleado,
            fechaHoraInicio=fechaHora,
            fecha_cambio=fechaHora 
        )
        nuevoCambioEstado.save()
        self.cambioEstado.add(nuevoCambioEstado)
        return nuevoCambioEstado

    # 26 Mostrar alcance
    def mostrarAlcance(self):
        return self.alcanceSismico.getDatosAlcance()
    
    # 30 Obtener clasificacion
    def obtenerDatosClasificacion(self):
        return self.clasificacion.getDatosClasificacion()
    
    # 34 Obtener origen
    def obtenerDatosOrigen(self):
        return self.origenGeneracion.getDatosOrigen()
    
    # 38 Obtener datos serie y muestras
    def obtenerDatosSerieYmuestra(self):
        return [serie.obtenerDatosMuestras() for serie in self.serieTemporal.all()]
    
    # 44 Obtener datos estacion
    def obtenerDatosEstacion(self):
        return [serie.obtenerDatosEstacion() for serie in self.serieTemporal.all()]

    def registrarRevision(self, fechaHoraActual, estado, empleado):
        self.crearCambioEstado(estado, fechaHoraActual, empleado)
        self.estadoActual = estado
        self.save()
    
    # 23 Crear cambio de estado
    def crearCE(self, estado: Estado, fechaHora: datetime,empleado=None):
        nuevoCambioEstado = CambioEstado(
            evento=self,
            estado=estado,
            empleado=empleado,
            fecha_cambio=fechaHora,
            fechaHoraInicio=fechaHora
        )
        nuevoCambioEstado.save()
        self.cambioEstado.add(nuevoCambioEstado)
        return nuevoCambioEstado

    # 20
    def bloquear(self, fechaHoraActual: datetime, estado: Estado) -> None:
        for i in self.cambioEstado.all():
            if i.esActual():
                i.setFechaHoraFin(fechaHoraActual)
                print(f"(: Cambio de estado actualizado: {i}")
                i.save()
        self.crearCE(estado, fechaHoraActual)
        self.estadoActual = estado
        self.save()