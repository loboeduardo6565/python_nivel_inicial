# Base de datos relacionales
# SQLite3


import sqlite3 

# Creando una BD 


conn = sqlite3.connect('basededatos.db') # Hay una rutina de sqlite llamado connect, te permite crear una BD si no existe, si existe simplemente la lee
conn.close()

# Invocando una BD a través de una función 

def crear_base(): # Puedo usar esta función cada vez que necesite crear una tabla
    conn = sqlite3.connect('basededatos.db') 
    return conn

crear_base()

"""
# Creando una tabla en la BD

def crear_tabla(conn):
    cursor = conn.cursor()
    sql = "CREATE TABLE repuestos(id integer PRIMARY KEY, nombre text)"
    cursor.execute(sql) # Ejecutar desde la BD
    conn.commit() # Grabar en BD 

conn = crear_base() # Llamo a la conexión de la BD
crear_tabla(conn)

"""
# Creando un registro en la BD

def insertar(conn, nombre):
    cursor = conn.cursor()
    data = (1, nombre) # Creo una tupla
    sql = "INSERT INTO repuestos(id, nombre) VALUES(?, ?)" # Se los pasaré 
    cursor.execute(sql, data) # Ejecutar desde la BD
    conn.commit() # Grabar en BD 

conn = crear_base() # Llamo a la conexión de la BD
insertar(conn, "Amortiguadores")