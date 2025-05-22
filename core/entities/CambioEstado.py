from django.db import models

class CambioEstado(models.Model):
    evento = models.ForeignKey('EventoSismico', related_name='cambios_estado', on_delete=models.CASCADE)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    fecha_cambio = models.DateTimeField()
    fechaHoraInicio = models.DateTimeField(null=True, blank=True)
    fechaHoraFin = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = 'core'
