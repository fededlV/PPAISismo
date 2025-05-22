from datetime import datetime
from dominio import MuestraSismica

class SerieTemporal:
    def __init__(self, condicionAlarma: bool, fechaHoraInicioRegistroMuestras: datetime, fechaHoraRegistro: datetime, frecuenciaMuestreo: float):
        self.condicionAlarma = condicionAlarma
        self.fechaHoraInicioRegistroMuestras = fechaHoraInicioRegistroMuestras
        self.fechaHoraRegistro = fechaHoraRegistro
        self.frecuenciaMuestreo = frecuenciaMuestreo
        self.muestras = []

