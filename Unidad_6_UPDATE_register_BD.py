# Actualizando un registro en una tabla

import mysql.connector # inicialmente se importa la librería

my_db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "qaz123..",
    database = "repuestos"
) 

my_cursor = my_db.cursor()


sql_inst = "UPDATE producto SET nombre = %s WHERE id = %s" # La instrucción, si tuviera que agregar más campos lo separo por coma, porcentaje vendría a ser el ? en SQLite
datos = ("Filtro de Gasolina", 1) # Creamos una tupla y le enviamos el valor que espera en la instrucción anterior con el %s 
my_cursor.execute(sql_inst, datos) # Le paso la instrucción y los valores de los parametros esperados como parametros 
my_db.commit() # Guardo los cambios

