# ==============================
# Clases del sistema universitario
# ==============================

class Nota:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo

    def get_valor(self):
        return self.valor

    def set_valor(self, v):
        self.valor = v


class Materia:
    def __init__(self, id_materia, nombre):
        self.id_materia = id_materia
        self.nombre = nombre
        self.notas = []
        self.promedio = 0.0

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        suma = sum(n.get_valor() for n in self.notas)
        self.promedio = suma / len(self.notas)
        return self.promedio


class Profesor:
    def __init__(self, id_profesor, nombre, especialidad):
        self.id_profesor = id_profesor
        self.nombre = nombre
        self.especialidad = especialidad
        self.cursos = []

    def dictar_curso(self, curso):
        self.cursos.append(curso)


class Estudiante:
    def __init__(self, id_estudiante, nombre, edad):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.edad = edad
        self.cursos = []

    def inscribirse_curso(self, curso):
        self.cursos.append(curso)

    def calcular_promedio_general(self):
        total = 0
        cantidad = 0
        for curso in self.cursos:
            promedio = curso.calcular_promedio()
            if promedio > 0:
                total += promedio
                cantidad += 1
        return total / cantidad if cantidad > 0 else 0


class Curso:
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.profesor = None
        self.notas = []

    def asignar_profesor(self, profesor):
        self.profesor = profesor
        profesor.dictar_curso(self)

    def registrar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        if not self.notas:
            return 0
        return sum(n.get_valor() for n in self.notas) / len(self.notas)


class Programa:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.estudiantes = []
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def inscribir_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)


class Facultad:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.programas = []

    def agregar_programa(self, programa):
        self.programas.append(programa)


class Universidad:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.facultades = []

    def agregar_facultad(self, facultad):
        self.facultades.append(facultad)


# ==============================
# Programa principal (main)
# ==============================

def main():
    print("=== Sistema Universitario ===\n")

    # Datos de la universidad
    nombre_uni = input("Ingrese el nombre de la universidad: ")
    direccion_uni = input("Ingrese la dirección de la universidad: ")
    uni = Universidad(nombre_uni, direccion_uni)

    # Facultad
    nombre_fac = input("\nIngrese el nombre de la facultad: ")
    codigo_fac = input("Ingrese el código de la facultad: ")
    fac = Facultad(nombre_fac, codigo_fac)
    uni.agregar_facultad(fac)

    # Programa
    nombre_prog = input("\nIngrese el nombre del programa académico: ")
    codigo_prog = input("Ingrese el código del programa: ")
    prog = Programa(nombre_prog, codigo_prog)
    fac.agregar_programa(prog)

    # Profesor
    id_prof = int(input("\nIngrese el ID del profesor: "))
    nombre_prof = input("Ingrese el nombre del profesor: ")
    especialidad_prof = input("Ingrese la especialidad del profesor: ")
    prof = Profesor(id_prof, nombre_prof, especialidad_prof)

    # Curso
    nombre_curso = input("\nIngrese el nombre del curso: ")
    codigo_curso = input("Ingrese el código del curso: ")
    creditos = int(input("Ingrese el número de créditos: "))
    curso = Curso(nombre_curso, codigo_curso, creditos)
    curso.asignar_profesor(prof)
    prog.agregar_curso(curso)

    # Estudiante
    id_est = int(input("\nIngrese el ID del estudiante: "))
    nombre_est = input("Ingrese el nombre del estudiante: ")
    edad_est = int(input("Ingrese la edad del estudiante: "))
    est = Estudiante(id_est, nombre_est, edad_est)
    est.inscribirse_curso(curso)
    prog.inscribir_estudiante(est)

    # Notas
    print("\n--- Registro de notas ---")
    while True:
        tipo_nota = input("Tipo de nota (Parcial, Final, Tarea): ")
        valor = float(input("Valor de la nota (0 a 5): "))
        nota = Nota(valor, tipo_nota)
        curso.registrar_nota(nota)

        continuar = input("¿Desea agregar otra nota? (s/n): ")
        if continuar.lower() != 's':
            break

    # Resultados
    promedio_curso = curso.calcular_promedio()
    promedio_general = est.calcular_promedio_general()

    print("\n===== RESUMEN =====")
    print(f"Universidad: {uni.nombre}")
    print(f"Facultad: {fac.nombre}")
    print(f"Programa: {prog.nombre}")
    print(f"Profesor: {prof.nombre} ({prof.especialidad})")
    print(f"Curso: {curso.nombre} - Promedio: {promedio_curso:.2f}")
    print(f"Estudiante: {est.nombre} - Promedio general: {promedio_general:.2f}")


# ==============================
# Ejecución
# ==============================
if __name__ == "__main__":
    main()
