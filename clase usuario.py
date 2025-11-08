class Usuario:
    """
    Clase base para manejar usuarios del sistema.
    """
    def __init__(self, idUsuario: int, nombre: str, correo: str, rol: str):
        self.__idUsuario = idUsuario
        self.__nombre = nombre
        self.__correo = correo
        self.__rol = rol
        self.__contrasena = None

    def registrarContrasena(self, contrasena: str):
        self.__contrasena = contrasena

    def iniciarSesion(self, correo: str, contrasena: str) -> bool:
        return self.__correo == correo and self.__contrasena == contrasena
