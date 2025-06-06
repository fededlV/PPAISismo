from django.db import models

class Empleado(models.Model):
    apellido = models.CharField(max_length=100)
    mail = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"Alcance {self.nombre}"
    class Meta:
        app_label = 'core'

    def getDatos(self):
        return {
            'apellido': self.apellido,
            'mail': self.mail,
            'nombre': self.nombre,
        }
