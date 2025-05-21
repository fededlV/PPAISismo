from django.db import models

class CambioEstado(models.Model):
    evento = models.ForeignKey('EventoSismico', related_name='cambios_estado', on_delete=models.CASCADE)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    fecha_cambio = models.DateTimeField()
    fechaHoraInicio = models.DateTimeField(null=True, blank=True)
    fechaHoraFin = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.evento} cambió a {self.estado} en {self.fecha_cambio}"