from django.db import models

class Estado(models.Model):
    ambito = models.CharField(max_length=50)  # Ej: "EventoSísmico"
    nombre_estado = models.CharField(max_length=50)  # Ej: "auto detectado", "confirmado", etc.

    def __str__(self):
        return f"{self.ambito} - {self.nombre_estado}"