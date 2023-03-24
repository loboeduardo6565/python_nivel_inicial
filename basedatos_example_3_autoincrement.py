# configurando un id automatico como primary key

import sqlite3

conn = sqlite3.connect("autorepuestos2.db")

cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE REPUESTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_P VARCHAR(20),
        PRECIO INTEGER, 
        CATEG_P VAARCHAR(20))

''')


repuestos = [
    ('Amortiguadores',20, 'Suspension' ),
    ('Espirales',30, 'Suspension' ),
    ('Alternador',50, 'Distribución' ),
]

cursor.executemany("INSERT INTO REPUESTOS VALUES (NULL,?,?,?)", repuestos)

conn.commit()
conn.close()