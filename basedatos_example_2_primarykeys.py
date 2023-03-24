import sqlite3

conn = sqlite3.connect("autorepuestos.db")

cursor = conn.cursor()

"""
cursor.execute('''
    CREATE TABLE REPUESTOS(
        CODIGO_P VARCHAR(10) PRIMARY KEY, 
        NOMBRE_P VARCHAR(20),
        CATEG_P VAARCHAR(20))

''')
"""

repuestos = [
    ('A01', 'Amortiguadores', 'Suspension' ),
    ('A02', 'Espirales', 'Suspension' ),
    ('A03', 'Alternador', 'Distribución' ),
]

cursor.executemany("INSERT INTO REPUESTOS VALUES(?,?,?)", repuestos)

conn.commit()
conn.close()