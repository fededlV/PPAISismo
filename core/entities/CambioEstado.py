from django.db import models

class CambioEstado(models.Model):
    evento = models.ForeignKey('EventoSismico', on_delete=models.CASCADE, related_name='cambios_estado',null=True, blank=True)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, null=True, blank=True)
    fecha_cambio = models.DateTimeField()
    fechaHoraInicio = models.DateTimeField(null=True, blank=True)
    fechaHoraFin = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.estado} ({self.fecha_cambio})"
    
    class Meta:
        app_label = 'core'

    # 21. Es actual
    def esActual(self):
        """Retorna True si este cambio de estado es el actual."""
        return self.fechaHoraFin is None

    # 22. Set fecha y hora de Fin
    def setFechaHoraFin(self, fechaHoraFin):
        """Establece la fecha y hora de fin del cambio de estado."""
        self.fechaHoraFin = fechaHoraFin
        self.save()
