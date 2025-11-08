class Materia:
    """
    Representa una materia específica dentro del programa académico.
    """
    def __init__(self, idMateria: int, nombre: str):
        self.__idMateria = idMateria
        self.__nombre = nombre
        self.__notas = []
        self.__promedio = 0.0

    def agregarNota(self, nota: Nota):
        self.__notas.append(nota)

    def calcularPromedio(self) -> float:
        if len(self.__notas) == 0:
            return 0
        suma = sum(n.getValor() for n in self.__notas)
        self.__promedio = suma / len(self.__notas)
        return self.__promedio

    def getPromedio(self):
        return self.__promedio

    def getNombre(self):
        return self.__nombre
