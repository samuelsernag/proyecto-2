class Universidad:
    """
    Representa una universidad con varias facultades.
    """
    def __init__(self, nombre: str, direccion: str):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__facultades = []

    def agregarFacultad(self, facultad: Facultad):
        self.__facultades.append(facultad)

    def obtenerFacultades(self):
        return self.__facultades
