import  from django.db import models
import from estado.models import Estado

class EventoSismico(models.Model):
    fecha_hora_fin = models.DateTimeField()
    fecha_hora_ocurrencia = models.DateTimeField()

    latitud_epicentro = models.FloatField()
    latitud_hipocentro = models.FloatField()
    longitud_epicentro = models.FloatField()
    longitud_hipocentro = models.FloatField()

    valor_magnitud = models.FloatField()

    estado = models.ForeignKey(
        Estado,
        on_delete=models.PROTECT,  # o CASCADE si querés que se borren los eventos con el estado
        related_name='eventos'
    )

    def __str__(self):
        return f"Evento {self.id} - {self.fecha_hora_ocurrencia.strftime('%Y-%m-%d %H:%M:%S')}"