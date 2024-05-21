from gestor_espacios_deportivos.database.almacen_info import AlmacenInfo
from gestor_espacios_deportivos.model.datos_objeto import EspacioDeportivo
from gestor_espacios_deportivos.model.usuario import Administrativo, General


class GestorED:
    @classmethod
    def agregar_espacio_deportivo(cls, id_espacio: int, nombre: str, reglamento: str, capacidad: int, db):
        espacio = EspacioDeportivo(id_espacio, nombre, reglamento, capacidad)
        db.registrar_espacio_deportivo(espacio)

    @classmethod
    def eliminar_espacio_deportivo(cls, id_espacio: int, db):
        for espacio in AlmacenInfo.EspaciosDeportivos:
            if espacio.id == id_espacio:
                db.eliminar_espacio_deportivo(espacio)


class GestorInicioSesion:

    @classmethod
    def registrar_administrativo(cls, documento: int, nombre: str, apellido: str, correo: str, contraseña: str, db):
        admin = Administrativo(documento, nombre, apellido, correo, contraseña)
        AlmacenInfo.Administrativos.append(admin)
        db.registrar_administrativo(admin)

    @classmethod
    def registrar_general(cls, documento: int, nombre: str, apellido: str, correo: str, contraseña: str, db):
        print("Registrarse como general...")
        general = General(documento, nombre, apellido, correo, contraseña)
        AlmacenInfo.Generales.append(general)
        db.registrar_general(general)

    @classmethod
    def iniciar_sesion_administrativo(cls, documento: int, ctr: str):
        for i in AlmacenInfo.Administrativos:
            if i.documento == documento and i.contraseña == ctr:
                return True
        return False

    @classmethod
    def iniciar_sesion_general(cls, documento: int, ctr: str):
        for i in AlmacenInfo.Generales:
            if i.documento == documento and i.contraseña == ctr:
                return True
        return False


class GestorReserva:
    @classmethod
    def mostrar_espacios_deportivo(cls):
        espacios = []
        # id_espacio, nombre, reglamento, capacidad
        for ed in AlmacenInfo.EspaciosDeportivos:
            e = {"Id": ed.id, "Nombre": ed.nombre, "Reglamento": ed.reglamento, "Capacidad": ed.capacidad}
            espacios.append(e)
        return espacios

    @classmethod
    def agendar_espacio_deportivo(cls, id_general: int, id_espacio: int, hora_inicio: int, hora_fin: int, db):
        for espacios in AlmacenInfo.EspaciosDeportivos:
            if espacios.id == id_espacio:
                db.agendar_reserva_ED(id_general, id_espacio, hora_inicio, hora_fin)
                return True
        return False

    @classmethod
    def mostrar_instructores(cls):
        instructores = []
        for ed in AlmacenInfo.Instructores:
            e = {"Documento": ed.documento, "Nombre": ed.nombre, "Apellido": ed.apellido, "Correo": ed.correo}
            instructores.append(e)
        return instructores

    @classmethod
    def agendar_instructor(cls, id_general: int, id_instructor: int, hora_inicio: int, hora_fin: int, db):
        for instructor in AlmacenInfo.Instructores:
            if instructor.documento == id_instructor:
                db.agendar_reserva_instructor(id_general, id_instructor, hora_inicio, hora_fin)
                return True
        return False

    @classmethod
    def mostrar_equipamiento(cls):
        equipamiento = []
        for ed in AlmacenInfo.Equipamientos:
            e = {"ID": ed.id, "Nombre": ed.nombre, "Cantidad": ed.cantidad}
            equipamiento.append(e)
        return equipamiento

    @classmethod
    def agendar_equipamiento(cls, id_general: int, id_equipamiento: int, hora_inicio: int, hora_fin: int, db):
        for equipamiento in AlmacenInfo.Equipamientos:
            if equipamiento.id == id_equipamiento:
                db.agendar_reserva_equipamiento(id_general, id_equipamiento, hora_inicio, hora_fin)
                return True
        return False

