from django.db import models

class CambioEstado(models.Model):
    evento = models.ForeignKey('EventoSismico', related_name='cambios_estado', on_delete=models.CASCADE)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, null=True, blank=True)
    fecha_cambio = models.DateTimeField()
    fechaHoraInicio = models.DateTimeField(null=True, blank=True)
    fechaHoraFin = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = 'core'

    def esActual(self):
        """Retorna True si este cambio de estado es el actual."""
        return self.fechaHoraFin is None

    def setFechaHoraFin(self, fechaHoraFin):
        """Establece la fecha y hora de fin del cambio de estado."""
        self.fechaHoraFin = fechaHoraFin
        self.save()
