
from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conn = ConexionDB()

    sql = '''
        CREATE TABLE warhammer(
            id_warhammer INTEGER,
            nombre VARCHAR(50),
            army VARCHAR(50),
            precio VARCHAR(10),
            minis VARCHAR(10),
            PRIMARY KEY (id_warhammer AUTOINCREMENT)
        )
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar()
        titulo = "Crear registro"
        msg = "Se ha creado la tabla en la Base de Datos"
        messagebox.showinfo(titulo, msg)
    except:
        titulo = "Crear registro"
        msg = "La tabla ya existe"
        messagebox.showwarning(titulo, msg)

def borrar_tabla():

    conn = ConexionDB()

    sql = '''
        DROP TABLE warhammer
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar()
        titulo = "Eliminar tabla"
        msg = "La tabla de la Base de Datos se borró con éxito"
        messagebox.showinfo(titulo, msg)
    except:
        titulo = "Eliminar tabla"
        msg = "No hay ninguna tabla que borrar en la Base de Datos"
        messagebox.showerror(titulo, msg)

class Warhammer:
    def __init__(self, nombre, army, precio, minis):
        self.id_warhammer = None
        self.nombre = nombre
        self.army = army
        self.precio = precio
        self.minis = minis

    def __str__(self):
        return f'Warhammer[{self.nombre}, {self.army}, {self.precio}, {self.minis}]'


def guardar(warhammer):
    conn = ConexionDB()
    sql = f"""INSERT INTO warhammer (nombre, army, precio, minis)
    VALUES ('{warhammer.nombre}', '{warhammer.army}', '{warhammer.precio}', '{warhammer.minis}')"""

    try:
        conn.cursor.execute(sql)
        conn.cerrar()
    except:
        titulo = "Insertar registro"
        msg = "La tabla warhammer no está creada en la Base de Datos"
        messagebox.showerror(titulo, msg)

def listar():
    conn = ConexionDB()
    lista_warhammer = []
    sql = '''SELECT * FROM warhammer'''

    try:
        conn.cursor.execute(sql)
        lista_warhammer = conn.cursor.fetchall()    #Recupera toda la info
        conn.cerrar()
    except:
        titulo = "Nuevo Registro"
        msg = "Crea la tabla en la base de dato"
        messagebox.showwarning(titulo, msg)

    return lista_warhammer

def editar(warhammer, id_warhammer):
    conn = ConexionDB()
    sql = f"""
        UPDATE warhammer
        SET nombre = '{warhammer.nombre}', army = '{warhammer.army}',precio = '{warhammer.precio}',minis = '{warhammer.minis}'
        WHERE id_warhammer = '{id_warhammer}'"""
        
    try:
        conn.cursor.execute(sql)
        conn.cerrar()
    except:
        titulo = "Edición de datos"
        msg = "No se ha podido modificar el registro"
        messagebox.showerror(titulo, msg)
        

def eliminar(id_warhammer):
    conn = ConexionDB()
    sql = f"""DELETE FROM warhammer WHERE id_warhammer = {id_warhammer}"""

    try:
        conn.cursor.execute(sql)
        conn.cerrar()
    except:
        titulo = 'Eliminar registro'
        msg = 'No se pudo eliminar el registro'
        messagebox.showerror(titulo, msg)
        



