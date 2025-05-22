from django.db import models

class CambioEstado(models.Model):
    evento = models.ForeignKey('EventoSismico', related_name='cambios_estado', on_delete=models.CASCADE)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    fecha_cambio = models.DateTimeField()
    fechaHoraInicio = models.DateTimeField(null=True, blank=True)
    fechaHoraFin = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = 'core'


    def esActual(self):
        """
        Verifica si el cambio de estado es el actual.
        :return: True si es el actual, False en caso contrario.
        """
        return self.fechaHoraFin is None
