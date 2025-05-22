from django.db import models

class Usuario(models.Model):
    contrasena = models.CharField(max_length=128)
    nombreUsuario = models.CharField(max_length=150, unique=True)

    class Meta:
        app_label = 'core'
