# DELETE

import sqlite3

conn = sqlite3.connect("autorepuestos2.db")

cursor = conn.cursor()

cursor.execute("DELETE FROM REPUESTOS WHERE ID=2")

conn.commit()
conn.close()