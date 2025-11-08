class Programa:
    """
    Representa un programa académico que contiene cursos y estudiantes.
    """
    def __init__(self, nombre: str, codigo: str):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__estudiantes = []
        self.__cursos = []

    def agregarCurso(self, curso: Curso):
        self.__cursos.append(curso)

    def inscribirEstudiante(self, estudiante: Estudiante):
        self.__estudiantes.append(estudiante)
        estudiante._Estudiante__programa = self

    def obtenerPromedios(self) -> float:
        total = 0
        cantidad = 0
        for e in self.__estudiantes:
            total += e.calcularPromedioGeneral()
            cantidad += 1
        return total / cantidad if cantidad > 0 else 0
