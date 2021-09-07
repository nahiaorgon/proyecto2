import sqlite3

def check_pw(email):
    connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT password FROM newusers WHERE email='{email}' ORDER BY pk DESC;""".format(email=email))
    password = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    return password


def check_users():
    connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT email FROM newusers ORDER BY pk DESC;""")
    db_newusers = cursor.fetchall()
    newusers=[]
    for i in range(len(db_newusers)):
        person = db_newusers[i][0]
        newusers.append(person)

    connection.commit()
    cursor.close()
    connection.close()
    
    return newusers




 #pagina de registro de usuario
def signup(name, lastname, email, password, profesorado):
    connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT email FROM newusers WHERE email = '{email}';""".format(email=email))
    exist = cursor.fetchone()

    if exist is None:
        cursor.execute("""INSERT INTO newusers(name, lastname, email, password, profesorado)VALUES('{name}', '{lastname}', '{email}', '{password}', '{profesorado}');""".format(name=name, lastname=lastname, email=email, password=password, profesorado=profesorado))
        connection.commit()
        cursor.close()
        connection.close()
    else: 
        return ('Usuario existente')
    return 'Te has registrado bien'