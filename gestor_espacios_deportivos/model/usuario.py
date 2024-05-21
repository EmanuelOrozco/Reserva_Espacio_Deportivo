class Usuario:
    def __init__(self, nombre: str, apellido: str, documento: int, correo: str, contraseña: str):
        self.nombre: str = nombre
        self.apellido: str = apellido
        self.documento: int = documento
        self.correo: str = correo
        self.contraseña: str = contraseña

class General(Usuario):

    def __init__(self, documento: int, nombre: str, apellido: str, correo: str, contraseña: str):
        super().__init__(nombre, apellido, documento, correo, contraseña)


class Administrativo(Usuario):
    def __init__(self, documento: int, nombre: str, apellido: str, correo: str, contraseña: str):
        super().__init__(nombre, apellido, documento, correo, contraseña)
