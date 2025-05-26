from django.db import models

class AlcanceSismo(models.Model):
    descripcion = models.TextField()
    nombre = models.CharField(max_length=255)

    def getDatosAlcance(self):
        """
        Obtiene los datos del alcance del sismo.
        :return: Diccionario con los datos del alcance.
        """
        return {
            'descripcion': self.descripcion,
            'nombre': self.nombre
        }