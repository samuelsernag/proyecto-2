class Facultad:
    """
    Representa una facultad dentro de la universidad.
    """
    def __init__(self, nombre: str, codigo: str, decano: Profesor):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__programas = []
        self.__decano = decano

    def agregarPrograma(self, programa: Programa):
        self.__programas.append(programa)

    def obtenerProgramas(self):
        return self.__programas
