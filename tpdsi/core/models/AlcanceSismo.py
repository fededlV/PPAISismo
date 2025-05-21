from django.db import models

class AlcanceSismo(models.Model):
    descripcion = models.CharField(max_length=255)
    nombre = models.CharField(max_length=100)

    def getDatosAlcance(self):
        return self.descripcion, self.nombre