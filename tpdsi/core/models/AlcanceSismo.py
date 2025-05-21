from django.db import models

class AlcanceSismo(models.Model):
    descripcion = models.TextField()
    nombre = models.CharField(max_length=255)

    def getDatosAlcance(self):
        return self.descripcion, self.nombre

    def __str__(self):
        return self.nombre