class Asignatura:
    """
    Representa una asignatura general que puede tener varios cursos.
    """
    def __init__(self, codigo: str, nombre: str, creditos: int):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__creditos = creditos
        self.__cursos = []

    def agregarCurso(self, curso):
        self.__cursos.append(curso)

    def obtenerCursos(self):
        return self.__cursos
