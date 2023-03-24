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
sql_inst = "DELETE FROM producto WHERE id = %s" # La instrucción, si tuviera que agregar más campos lo separo por coma, porcentaje vendría a ser el ? en SQLite
datos = ("1",) # Creamos una tupla y le enviamos el valor que espera en la variable anterior con el %s 
my_cursor.execute(sql_inst, datos) # Le paso las variables anteriores como parametros

my_db.commit() #Aplicando los cambios en la BD