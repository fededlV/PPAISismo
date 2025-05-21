from datetime import datetime

class CambioEstado:
    def __init__(self, fechaHoraInicio: datetime, fechaHoraFin: datetime):
        self.fechaHoraInicio: datetime = fechaHoraInicio
        self.fechaHoraFin: datetime = fechaHoraFin