# Creando una consulta en una tabla

import mysql.connector # inicialmente se importa la librería
my_db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "qaz123..",
    database = "repuestos"
) 

my_cursor = my_db.cursor()


# Generando la consulta por el campo nombre
# nombre = "nombre"
sql_inst = "SELECT * FROM producto WHERE id = %s AND  nombre =%s" # La instrucción, si tuviera que agregar más campos lo separo por coma, porcentaje vendría a ser el ? en SQLite
datos = (1, "Filtro",) # Creamos una tupla y le enviamos el valor que espera en la variable anterior con el %s 
my_cursor.execute(sql_inst, datos) # Le paso las variables anteriores como parametros

consulta = my_cursor.fetchall()

for filas in consulta:
    print(filas)

