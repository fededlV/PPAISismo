from django.db import models

class EstacionSismologica(models.Model):
    codigoEstacion = models.CharField(max_length=50, unique=True)
    documentoCertificacionAdq = models.CharField(max_length=255)
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    nroCertificacionAdquisicion = models.IntegerField()

    class Meta:
        app_label = 'core'

