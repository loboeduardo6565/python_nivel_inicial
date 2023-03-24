# UPDATE

import sqlite3

conn = sqlite3.connect("autorepuestos2.db")

cursor = conn.cursor()

cursor.execute("UPDATE REPUESTOS SET CATEG_P='Suspensión' WHERE CATEG_P='Suspension'")
consulta = cursor.fetchall()
for registro in consulta:
    print(registro)

conn.commit()
conn.close()