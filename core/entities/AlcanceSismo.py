from django.db import models

class AlcanceSismo(models.Model):
    descripcion = models.TextField()
    nombre = models.CharField(max_length=255)

    