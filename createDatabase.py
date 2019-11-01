"""
Este archivo sirve para crear la base de datos. Debe correrse antes que saveLink.py
Tener cuidado que el nombre de la base hay que cambiarlo en saveLink.py en caso
de usar uno diferente a 'save_message_db.sqlite'
"""


import sqlite3

conn = sqlite3.connect('save_message_db.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE links (date VARCHAR, user VARCHAR, link VARCHAR)')
conn.commit()

conn.close()
