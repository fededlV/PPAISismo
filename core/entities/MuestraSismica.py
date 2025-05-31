from datetime import datetime
from django.db import models

class MuestraSismica(models.Model):
    def __init__(self, fechaHoraMuestra: datetime):
        self.fechaHoraMuestra = fechaHoraMuestra
        self.detalles = []
        
    def __str__(self):
        return f"Evento {self.id} - {self.fechaHoraMuestra}"
    
    def obtenerDenominacionYValor(self):
        pass


