from django.db import models

class CambioEstado(models.Model):
    evento = models.ForeignKey('EventoSismico', related_name='cambios_estado', on_delete=models.CASCADE)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, null=True, blank=True)
    fecha_cambio = models.DateTimeField() #ESTE ATRIBUTO PARA QUE SIRVE? A QUE HACE REFERENCIA EN EL DIAGRAMA DE CLASES?
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

    def setFechaHoraFin(self, fecha_Hora_Fin):
        """
        Establece la fecha y hora de fin del cambio de estado.
        :param fechaHoraFin: Fecha y hora de fin.
        """
        self.fechaHoraFin = fecha_Hora_Fin
        self.save()
