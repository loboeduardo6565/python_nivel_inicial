# Creando una tabla en una BD MariaDB

import mysql.connector # inicialmente se importa la librería
my_db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "qaz123..",
    database = "repuestos"
) 

my_cursor = my_db.cursor()


# Generando la consulta por id. 
sql_inst = "SELECT * FROM producto WHERE id = %s" # La instrucción, si tuviera que agregar más campos lo separo por coma, porcentaje vendría a ser el ? en SQLite
datos = ("2",) # Creamos una tupla y le enviamos el valor que espera en la variable anterior con el %s 
my_cursor.execute(sql_inst, datos) # Le paso las variables anteriores como parametros

consulta = my_cursor.fetchall()

for filas in consulta:
    print(filas)


# Generando la consulta para todos los registros. 
sql_inst = "SELECT * FROM producto" # La instrucción de consulta
my_cursor.execute(sql_inst) # Le paso la variable anterior como parametro

consulta = my_cursor.fetchall()

for filas in consulta: # Creamor un bucle que recorra todas las filas que trae la consulta 
    print(filas)