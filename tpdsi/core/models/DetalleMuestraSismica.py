


class DetalleMuestraSismica:
    def __init__(self, valor: int):
        self.valor = valor
        self.tipoDato = None
    
    def obtenerDenominacionYValor(self):
        if self.tipoDato != None:
            return self.tipoDato.obtenerDenominacion()
        else:
            return "No tiene tipo de dato registrado"