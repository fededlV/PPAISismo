from datetime import datetime
from dominio import DetalleMuestraSismica

class MuestraSismica:
    def __init__(self, fechaHoraMuestra: datetime):
        self.fechaHoraMuestra = fechaHoraMuestra
        self.detalles = []
    
    def obtenerDenominacionYValor(self):
        if self.detalles != []: 
            return [detalle.obtenerDenominacionYValor() for detalle in self.detalles]
        else: 
            return "No hay detalles registrados"
    
    def agregarDetalle(self, detalle: DetalleMuestraSismica):
        self.detalles.append(detalle)

    