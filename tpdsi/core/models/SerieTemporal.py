from datetime import datetime
from models import MuestraSismica

class SerieTemporal:
    def __init__(self, condicionAlarma: bool, fechaHoraInicioRegistroMuestras: datetime, fechaHoraRegistro: datetime, frecuenciaMuestreo: float):
        self.condicionAlarma = condicionAlarma
        self.fechaHoraInicioRegistroMuestras = fechaHoraInicioRegistroMuestras
        self.fechaHoraRegistro = fechaHoraRegistro
        self.frecuenciaMuestreo = frecuenciaMuestreo
        self.muestras = []

    def obtenerDatosMuestras(self):
        if self.muestras:
            return [muestra.obtenerDenominacionYValor() for muestra in self.muestras]
        else:
            return "No hay muestras registradas"


    def agregarMuestra(self, muestra: MuestraSismica):
        self.muestras.append(muestra)

