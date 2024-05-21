from gestor_espacios_deportivos.database.db import DB
from gestor_espacios_deportivos.ui.interfaz_grafica import Interfaz

# si la conexión a la base de datos se da, entonces ejecuta el programa
db = DB('app.db')
if db.conectar():
    # crear los objetos de toda la información de la base de datos
    db.obtener_administrativos()
    db.obtener_generales()
    db.obtener_espacios_deportivos()
    db.obtener_instructores()
    db.obtener_equipamientos()
    interfaz = Interfaz(db)
    interfaz.mostrar()
    db.desconectar()
