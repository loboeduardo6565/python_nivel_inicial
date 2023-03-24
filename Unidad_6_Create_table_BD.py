# Creando una tabla en una BD MariaDB

import mysql.connector # inicialmente se importa la librería
my_db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "qaz123..",
    database = "repuestos"
) 

my_cursor = my_db.cursor()
my_cursor.execute("CREATE TABLE producto(id int(7) NOT NULL PRIMARY KEY AUTO_INCREMENT, \
                  nombre VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL)")