from gestor_espacios_deportivos.model.usuario import Usuario


class EspacioDeportivo:

    def __init__(self, id: int, nombre: str, reglamento: str, capacidad: int):
        self.id: int = id
        self.nombre: str = nombre
        self.reglamento: str = reglamento
        self.capacidad: int = capacidad


class Equipamiento:
    def __init__(self, id: int, nombre: str, cantidad: int):
        self.id: int = id
        self.nombre: str = nombre
        self.cantidad: int = cantidad


class Instructor(Usuario):
    def __init__(self, documento: int, nombre: str, apellido: str, correo: str, contraseña: str,
                 espacio_deportivo: str):

        super().__init__(nombre, apellido, documento, correo, contraseña)
