# configurando un id automatico como primary key

import sqlite3

conn = sqlite3.connect("autorepuestos2.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM REPUESTOS WHERE CATEG_P='Suspension'")
consulta = cursor.fetchall()
for registro in consulta:
    print(registro)

#conn.commit()
conn.close()