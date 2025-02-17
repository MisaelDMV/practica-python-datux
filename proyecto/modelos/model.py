import sqlite3
from sqlite3 import Connection

class Autor:
    """ Tabla Autor con id y nombre """
    def create_table(self, con: Connection):
        query = """
        CREATE TABLE IF NOT EXISTS Autor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        );
        """
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()

class Editorial:
    """ Tabla Editorial con id y nombre """
    def create_table(self, con: Connection):
        query = """
        CREATE TABLE IF NOT EXISTS Editorial (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        );
        """
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()

class Libro:
    """
    Tabla Libro con:
    - id
    - titulo
    - isbn
    - precio
    - autor_nombre (texto, simplificado)
    - editorial_nombre (texto, simplificado)
    """
    def create_table(self, con: Connection):
        query = """
        CREATE TABLE IF NOT EXISTS Libro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL,
            precio REAL NOT NULL,
            autor_nombre TEXT NOT NULL,
            editorial_nombre TEXT NOT NULL
        );
        """
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
