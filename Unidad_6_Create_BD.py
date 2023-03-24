# Creando una BD con MariaDB

import mysql.connector # inicialmente se importa la librería
my_db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "qaz123.."
) 

my_cursor = my_db.cursor()
my_cursor.execute("CREATE DATABASE repuestos")