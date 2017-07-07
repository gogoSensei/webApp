#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask,render_template, request, make_response
#IRM 20/02/2017 La librerria realizo cambios ahora se llama CSRFProtect y anteriormente csrfProtect
from flask_wtf import CSRFProtect
from flask import session, redirect, url_for, config, g
from flask import flash
from flask_socketio import SocketIO
from db import run_query
import forms

app = Flask(__name__)
app.secret_key = 'angelesyoshua'
csrf = CSRFProtect(app)
socketio = SocketIO(app)
url_fac = 'https://www.facebook.com/isidro.rivera.37201'
url_twitter = 'https://twitter.com/kmotin818'
url_goo = 'https://plus.google.com/u/0/'

# Se agrega methods=['GET', 'POST'] para acceder desde las dos caracterirsticas
@app.route('/', methods=['GET', 'POST'])
def inicio():
    coment_form = forms.iniForm(request.form)
    #success_message = 'Bienvenido {0}'.format(coment_form.username.data)
    #flash(success_message)
    response = make_response(render_template('index.html',
                            title='Single Play',
                            url_face=url_fac,
                            url_twitters=url_twitter,
                            url_google=url_goo,
                            form = coment_form))
    return response

@app.route('/logOut', methods=['GET', 'POST'])
def logOut():
    #IRM 20/02/2017 eleiminar mi session creada
    if 'username' in session:
        session.pop('username')
        session.pop('mail')
        session.pop('coment')
    #custome_cookies = request.cookies.get('custome_cookies', 'undefinid')
    #response.set_cookies('custome_cookies', 'Isidro')
    return redirect(url_for('inicio'))

@app.route('/register', methods=['POST'])
def register():
    #JCGE 06/06/2017: Que onda que pez, aqui registramos al hijo de puta
    lista = ''
    coment_form = forms.iniForm(request.form)
    #success_message = 'Bienvenido {0}'.format(coment_form.username.data)
    #flash(success_message)
    print('hola perro' + g.test)# llama variable local
    if (request.method in ['POST'] and coment_form.validate()):
        lista = coment_form.username.data + ',' + coment_form.email.data + ',' + coment_form.comment.data
        session['username'] = coment_form.username.data
        session['mail'] = coment_form.email.data
        session['coment'] = coment_form.comment.data
    query = "INSERT INTO directorio VALUES ('{0}','{1}','{2}')".format(coment_form.username.data, coment_form.email.data, coment_form.comment.data)
    x = run_query(query)
    response = make_response(render_template('lobby.html',
                            title='Inicio',
                            form = coment_form))
    response.set_cookie('listData', lista)
    return response

@app.route('/juego', methods=['GET', 'POST'])
def juego():
    #JCGE 25/06/2017: redireccionamos a la pagina del juego
    response = make_response(render_template('juego.html',
                            title='Juego'))
    return response

@app.errorhandler(404)
def notFound(e):
    return render_template('404.html'), 404

@app.before_request
def beforeRequest():
    g.test = 'test'# Se declara variables globales y se tilizaran en cualquier funsion
    #if 'username' not in session:
    #x = run_query('SELECT * FROM directorio')
    #print(x)
    print(request.endpoint)
    #return render_template("index.html")

@app.after_request
def afterRequest(response):
    print("hola after request")
    print(g.test) # llama variable local
    #print(session)
    return response

@socketio.on('message')
def handle_message(message):
    print('mensaje recibido: ' + message)

#@socketio.on('json')
#def handle_json(json):
#    print('json recibido: ' + str(json))

@socketio.on('my event')
def handle_my_custom_event(json):
    print('json recibido: ' + str(json))
    return 'one', 2

if (__name__=='__main__'):
    #app.run(debug=True, port=5000)
    socketio.run(app)