from datetime import datetime
from dominio import DetalleMuestraSismica

class MuestraSismica:
    def __init__(self, fechaHoraMuestra: datetime):
        self.fechaHoraMuestra = fechaHoraMuestra
        self.detalles = []
    

    