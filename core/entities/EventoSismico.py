from django.db import models
from .Estado import Estado
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
    cambioEstado = models.ManyToManyField(CambioEstado, related_name='eventos_cambios_estado')
    analistaSuperior = models.ForeignKey(Empleado, on_delete=models.PROTECT, related_name='eventos_analista_superior', null=True, blank=True)
    
    def __str__(self):
        return f"Evento {self.id} - {self.estadoActual}"
    
    class Meta:
        app_label = 'core'

    # 5 Obtener eventos sismicos
    def obtenerEventosAd(self):
        a = self.estadoActual.ambitoEventoSismico()
        b = self.estadoActual.esAutoDetectado()
        c = self.estadoActual.esPendienteRevision()
        return a and (b or c)
    
    # 9 Obtener datos del evento sismico
    def getDatosEventoSismico(self):
        return {
            'id': self.id,
            'fechaHoraFin': self.get_fechaHoraFin(),
            'fechaHoraOcurrencia': self.get_fechaHoraOcurrencia(),
            'latitudEpicentro': self.get_latitudEpicentro(),
            'latitudHipocentro': self.get_latitudHipocentro(),
            'longitudEpicentro': self.get_longitudEpicentro(),
            'longitudHipocentro': self.get_longitudHipocentro(),
            'valorMagnitud': self.get_valorMagnitud(),
            'estadoActual': self.estadoActual.getNombreEstado(),
            'ambitoEstado': self.estadoActual.getAmbito(),  # <-- agrega esta línea
        }
        """ 'serieTemporal': self.serieTemporal,
            'cambioEstado': self.cambioEstado,
            'analistaSuperior': self.analistaSuperior.getDatos() """ # <- Esto no creo que sea necesario para cuando busca los datos del evento. 
    
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
    

    # 20
    def bloquear(self, fechaHoraActual: datetime, estado: Estado) -> None:
        self.crearCambioEstado(estado=estado, fechaHora=fechaHoraActual)
        self.estadoActual = estado
        self.save()

    def get_fechaHoraFin(self):
        return self.fechaHoraFin

    def get_fechaHoraOcurrencia(self):
        return self.fechaHoraOcurrencia

    def get_latitudEpicentro(self):
        return self.latitudEpicentro

    def get_latitudHipocentro(self):
        return self.latitudHipocentro

    def get_longitudEpicentro(self):
        return self.longitudEpicentro

    def get_longitudHipocentro(self):
        return self.longitudHipocentro

    def get_valorMagnitud(self):
        return self.valorMagnitud

    def get_estadoActual(self):
        return self.estadoActual

    def get_alcanceSismico(self):
        return self.alcanceSismico

    def get_clasificacion(self):
        return self.clasificacion

    def get_origenGeneracion(self):
        return self.origenGeneracion

    def get_serieTemporal(self):
        return self.serieTemporal

    def get_cambioEstado(self):
        return self.cambioEstado

    def get_analistaSuperior(self):
        return self.analistaSuperior