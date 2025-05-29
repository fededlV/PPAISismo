from datetime import datetime
from django.db import models

class MuestraSismica(models.Model):
    def __init__(self, fechaHoraMuestra: datetime):
        self.fechaHoraMuestra = fechaHoraMuestra
        self.detalles = []

    def obtenerDenominacionYValor(self):
        pass


