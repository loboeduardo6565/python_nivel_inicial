# Creando una tabla en una BD MariaDB

import mysql.connector # inicialmente se importa la librería
my_db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "qaz123..",
    database = "repuestos"
) 

my_cursor = my_db.cursor()

# Generando la Instrucción en pasos. 
sql_inst = "INSERT INTO producto (nombre) VALUES (%s)" # La instrucción, si tuviera que agregar más campos lo separo por coma, porcentaje vendría a ser el ? e SQLite
datos = ("Filtro de Aceite",) # Creamos una tupla
my_cursor.execute(sql_inst, datos) # Le paso las variables anteriores como parametros

my_db.commit() #Guardando el registro


