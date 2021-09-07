from flask import Flask, render_template, request, session, redirect, url_for, g
from flask import *
from flask_mail import *


import primerdatamodel
import sqlite3

app = Flask(__name__)
app.secret_key = 'jumpjacks'
mail= Mail(app)

app.config['MAIL_SERVER'] ='smtp.gmail.com'
app.config['MAIL_PORT '] = 587
app.config['MAIL_USERNAME'] = 'naahiiaariittaa@gmail.com'
app.config['MAIL_PASSWORD'] = 'visheriita-.-'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

user = primerdatamodel.check_users()

conexion = sqlite3.connect('flask_tut.db')
cursor = conexion.cursor()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        session.pop('email', None)
        temail=request.form.get('email')
        tpassword=request.form.get('password')
        pwd = primerdatamodel.check_pw(temail, tpassword)
        if request.form['password'] == pwd:
            #session['email'] = request.form['email']        
            cursor.execute("SELECT email FROM newusers") #Recuperamos los registros de la tabla de usuarios
            usuarios = cursor.fetchall() #Recorremos todos los registros con fetchall y los volcamos en una lista de usuarios
            for correo in usuarios:# Ahora podemos recorrer todos los usuarios
                print(usuarios[3])
                print(usuarios[4])
                print(usuarios[5])
                email_recuperado = usuarios[3]
                password_recuperada = usuarios[4]
                tipo_profesorado = usuarios[5]
    return render_template('log.html')

 

@app.route('/signup', methods=['GET', 'POST']) #pagina de registro de usuario (en primerdatemodel sigue)
def signup():
    if request.method =='GET':
    #ingresa por pantalla los datos
        name=request.form.get('name')
        lastname=request.form.get('lastname')
        email=request.form.get('email')
        password=request.form.get('password')
        profesorado=request.form.get('profesorado')
        mensaje = primerdatamodel.signup(name, lastname, email, password, profesorado) 
        return render_template('signup.html')
        #manda el correo (no anda)
        #msg = Message('Hola {name}, ¡te damos la bienvenida al Campus Virtual!'.format(name = name), sender = app.config['MAIL_USERNAME'], recipients = [email])
        #msg.body = "Hello Flask message sent from Flask-Mail"
        #mail.send(msg) 
    else:    
        return redirect(url_for('CAMPUSVIRTUAL_Historia'))

 

@app.route('/paginaprincipal', methods=['GET', 'POST'])
def paginaprincipal():
    return render_template('index.html')

@app.route('/visitantes', methods=['GET', 'POST'])
def visitantes():
    return render_template('visit.html')



@app.route('/CAMPUSVIRTUAL_Historia', methods=['GET', 'POST'])
def CAMPUSVIRTUAL_Historia():
    return render_template('cvHistoria.html')
 




@app.route('/docentes', methods=['GET', 'POST'])
def docentes():
    return render_template('doc.html')

@app.route('/profesoradoEconomia', methods=['GET', 'POST'])
def profesoradoEconomia():
    return render_template('profeconomia.html')

@app.route('/profesoradoHistoria', methods=['GET', 'POST'])
def profesoradoHistoria():
    return render_template('profhistoria.html')

@app.route('/profesoradoGeografia', methods=['GET', 'POST'])
def profesoradoGeografia():
    return render_template('profegeografia.html')

@app.route('/profesoradoCienciasPoliticas', methods=['GET', 'POST'])
def profesoradoCienciasPoliticas():
    return render_template('profCsPoliticas.html')





if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 7000, debug = True)

conexion.close()

#nahiaorgon@China:/mnt/c/Users/Nahia/Documents/Pirple$