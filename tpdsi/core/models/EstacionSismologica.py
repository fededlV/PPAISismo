class EstacionSismologica:
    def __init__(self, codigoEstacion: str, documentoCertificacionAdq: str, nombre: str, 
                 latitud: float, longitud: float, nroCertificacionAdquisicion: int):
        self.codigoEstacion = codigoEstacion
        self.documentoCertificacionAdq = documentoCertificacionAdq
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.nroCertificacionAdquisicion = nroCertificacionAdquisicion
        
    def getCodigoEstacion(self) -> str:
        return self.codigoEstacion