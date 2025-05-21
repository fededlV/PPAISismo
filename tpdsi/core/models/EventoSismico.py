from datetime import datetime

class EventoSismico:
    def __init__(self, fechaHoraFin: datetime, fechaHoraOcurrencia: datetime, latitudEpicentro: float, 
                 latitudHipocentro: float, longitudEpicentro: float, longitudHipocentro: float, valorMagnitud: float):
        self.fechaHoraFin = fechaHoraFin
        self.fechaHoraOcurrencia = fechaHoraOcurrencia
        self.latitudEpicentro = latitudEpicentro
        self.latitudHipocentro = latitudHipocentro
        self.longitudEpicentro = longitudEpicentro
        self.longitudHipocentro = longitudHipocentro
        self.valorMagnitud = valorMagnitud

    def obtenerEventosAD(eventos: int):
        for evento in eventos:
            if evento.fechaHoraOcurrencia > datetime.now():
                return evento
