class TipoDeDato:
    def __init__(self, denominacion: str, nombreUnidadMedida: str, valorUmbral: float):
        self.denominacion = denominacion
        self.nombreUnidadMedida = nombreUnidadMedida
        self.valorUmbral = valorUmbral

    def obtenerDenominacionYValor(self): 
        return f"{self.denominacion} ({self.valorUmbral})"
    def getDenominacion(self):
        return self.denominacion
    def getValorUmbral(self):
        return self.valorUmbral