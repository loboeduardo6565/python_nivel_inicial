import sqlite3

conn = sqlite3.connect("FirstDB.db") # Establecemos la conexión

cursor = conn.cursor()
# cursor.execute("CREATE TABLE USERS(NOMBRE VARCHAR(50), EDAD INTEGER, SEXO VARCHAR(50))") # Creamos una tabla 

# cursor.execute("INSERT INTO USERS VALUES('Carlos',38,'Masculino')")

"""
cursor.execute("SELECT * FROM USERS")
usuario = cursor.fetchone() # Crea una tupla
print(usuario)
print(usuario[0]) # Con lo cual podemos recorrerla desde un indice
print(usuario[1])
print(usuario[2])

"""

""" ************ Agregando registros de forma masiva ************

registros = [ # En forma de lista y a través de tuplas le envío varios registros
    ('Carla',35,'Femenino'), 
    ('Carlota',5,'Femenino'),
    ('José',38,'Masculino'), # Recuerda que las tuplas terminan con una coma siempre
]

cursor.executemany("INSERT INTO USERS VALUES(?,?,?)",registros) # concatenamos la lista

"""

cursor.execute("SELECT * FROM USERS")
usuarios = cursor.fetchall() # Imprime todos
print(usuarios) # Imprime por registros
for registros in usuarios:
    print(registros)


conn.commit() # Para impactar la query anterior 

conn.close()