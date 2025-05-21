class Usuario:
    def __init__(self, contrasena: str, nombreUsuario: str):
        self.contrasena = contrasena
        self.nombreUsuario = nombreUsuario
    def getASLogueado(self):
        return self.nombreUsuario