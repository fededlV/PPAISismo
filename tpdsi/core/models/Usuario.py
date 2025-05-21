from django.db import models

class Usuario(models.Model):
    contrasena = models.CharField(max_length=128)
    nombreUsuario = models.CharField(max_length=150, unique=True)

    def getASLogueado(self):
        return self.nombreUsuario

    def __str__(self):
        return self.nombreUsuario