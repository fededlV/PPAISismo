class Empleado:
    def __init__(self, apellido: str, mail: str, nombre: str, telefono: int, logueado: bool):
        self.apellido = apellido
        self.mail = mail
        self.nombre = nombre
        self.telefono = telefono
        self.logueado = logueado