from django.db import models

class AlcanceSismico(models.Model):
    descripcion = models.TextField()
    nombre = models.CharField(max_length=255)

    # 27 Get datos del alcance del sismo
    def getDatosAlcance(self):
        return {
            'descripcion': self.descripcion,
            'nombre': self.nombre
        }
