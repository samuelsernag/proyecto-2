from datetime import date

class Nota:
    def __init__(self, valor: float, fecha: date, tipo: str):
        self.__valor = valor
        self.__fecha = fecha
        self.__tipo = tipo

    def getValor(self) -> float:
        return self.__valor

    def setValor(self, v: float):
        self.__valor = v
