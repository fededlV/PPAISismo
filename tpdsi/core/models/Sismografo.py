from django.db import models

class Sismografo(models.Model):
    fechaHoraAdquisicion = models.DateTimeField()
    identificadorSismografo = models.CharField(max_length=100)
    nroSerie = models.IntegerField()
    # Suponiendo que existe un modelo Estacion, puedes descomentar la siguiente línea:
    # estacion = models.ForeignKey('Estacion', null=True, blank=True, on_delete=models.SET_NULL)

    def obtenerDatosEstacion(self):
        if hasattr(self, 'estacion') and self.estacion:
            return self.estacion.getCodigo()
        else:
            return "No tiene estación asociada"
