class Curso:
    """
    Representa un curso dictado dentro de una asignatura.
    """
    def __init__(self, nombre: str, codigo: str, creditos: int):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__creditos = creditos
        self.__profesor = None
        self.__notas = []

    def asignarProfesor(self, profesor: Profesor):
        self.__profesor = profesor
        profesor.dictarCurso(self)

    def registrarNota(self, nota: Nota):
        self.__notas.append(nota)

    def calcularPromedio(self) -> float:
        if len(self.__notas) == 0:
            return 0
        total = sum(n.getValor() for n in self.__notas)
        return total / len(self.__notas)
