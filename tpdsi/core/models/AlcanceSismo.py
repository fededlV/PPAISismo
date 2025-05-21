class AlcanceSismo:
    def __init__(self, descripcion: str, nombre: str):
        self.descripcion = descripcion
        self.nombre = nombre
    def getDatosAlcance(self):
        return self.descripcion, self.nombre
    