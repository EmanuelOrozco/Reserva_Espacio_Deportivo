from gestor_espacios_deportivos.model.datos_objeto import EspacioDeportivo, Instructor, Equipamiento
from gestor_espacios_deportivos.model.usuario import Administrativo, General


class AlmacenInfo:
    Administrativos: [Administrativo] = []
    Generales: [General] = []
    EspaciosDeportivos: [EspacioDeportivo] = []
    Instructores: [Instructor] = []
    Equipamientos: [Equipamiento] = []
