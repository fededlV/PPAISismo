import datetime


class Sismografo:
    def __init__(self, fechaHoraAdquisicion: datetime, identificadorSismografo: str, nroSerie: int):
        self.fechaHoraAdquisicion = fechaHoraAdquisicion
        self.identificadorSismografo = identificadorSismografo
        self.nroSerie = nroSerie
        self.estacion = None  # Inicializar la estación como None

    def obtenerDatosEstacion(self):
        if self.estacion:
            return self.estacion.getCodigo()
        else:
            return "No tiene estación asociada"
