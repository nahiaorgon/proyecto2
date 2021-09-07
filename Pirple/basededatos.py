import sqlite3 

connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE newusers(
        pk INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR(16),
        lastname VARCHAR(16),
        email VARCHAR(32),
        password VARCHAR(32),
        profesorado VARCHAR(32)
    );"""
)

connection.commit()
cursor.close()
connection.close()