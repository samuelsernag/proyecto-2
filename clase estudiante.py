class Estudiante:
    """
    Representa un estudiante con cursos y notas asociadas.
    """
    def __init__(self, idEstudiante: int, nombre: str, edad: int):
        self.__idEstudiante = idEstudiante
        self.__nombre = nombre
        self.__edad = edad
        self.__programa = None
        self.__cursos = []

    def inscribirseCurso(self, curso):
        self.__cursos.append(curso)

    def calcularPromedioGeneral(self) -> float:
        total = 0
        cantidad = 0
        for curso in self.__cursos:
            total += curso.calcularPromedio()
            cantidad += 1
        return total / cantidad if cantidad > 0 else 0
