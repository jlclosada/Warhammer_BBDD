import sqlite3

class ConexionDB:
    def __init__(self):
        self.base_datos = 'database/warhammer.db'
        self.conn = sqlite3.connect(self.base_datos)
        self.cursor = self.conn.cursor()
    
    def cerrar(self):
        self.conn.commit()
        self.conn.close()


