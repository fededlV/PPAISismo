from django.db import models

class EstacionSismologica(models.Model):
    codigoEstacion = models.CharField(max_length=50, unique=True)
    documentoCertificacionAdq = models.CharField(max_length=255)
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    nroCertificacionAdquisicion = models.IntegerField()

    def __str__(self):
        return f"Alcance {self.nombre}"
    class Meta:
        app_label = 'core'

    # 47
    def getCodigo(self):
        return self.codigoEstacion