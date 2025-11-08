from datetime import date

class CalendarioAcademico:
    """
    Representa los eventos académicos del semestre.
    """
    def __init__(self, semestre: str):
        self.__semestre = semestre
        self.__eventos = []

    def agregarEvento(self, fecha: date, descripcion: str):
        self.__eventos.append((fecha, descripcion))

    def listarEventos(self):
        return self.__eventos
