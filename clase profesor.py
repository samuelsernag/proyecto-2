class Profesor:
    """
    Representa un profesor que dicta uno o varios cursos.
    """
    def __init__(self, idProfesor: int, nombre: str, especialidad: str):
        self.__idProfesor = idProfesor
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__cursos = []

    def dictarCurso(self, curso):
        self.__cursos.append(curso)

    def listarCursos(self):
        return self.__cursos
