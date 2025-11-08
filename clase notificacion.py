from datetime import date

class Notificacion:
    """
    Representa una notificación enviada a un estudiante.
    """
    def __init__(self, mensaje: str, fecha: date, estudiante, curso):
        self.__mensaje = mensaje
        self.__fecha = fecha
        self.__estudiante = estudiante
        self.__curso = curso
        self.__leida = False

    def marcarLeida(self):
        self.__leida = True

    def mostrar(self):
        estado = "Leída" if self.__leida else "No leída"
        return f"[{estado}] {self.__mensaje} - {self.__curso} ({self.__fecha})"
