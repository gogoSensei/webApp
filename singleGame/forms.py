#!/usr/bin/env python
#-*- coding: utf-8 -*-

from wtforms import Form
from wtforms import StringField, TextField,TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from wtforms import HiddenField

#def 

class iniForm(Form):
    """docstring for iniForm"""
    #def __init__(self, arg):
    #	super(iniForm, self).__init__()
    #	self.arg = arg
    username = StringField('Nombre', 
                            [
                            validators.length(min=4, max=25, message= '¡Ingrese un usuario valido!'),
                            validators.Required(message = 'El usuario es requerido.')
                            ])
    email = EmailField('Correo electronico',
                       [
                        validators.Email(message='¡Ingrese un email valido!'),
                        validators.Required(message = 'El email es requerido.')
                       ])
    comment = TextAreaField('Comentario',
                            [
                            validators.length(min=4, max=146, message='¡Ingresar mensaje valido!'),
                            validators.Required(message='¡Es necesario ingresar un mensaje que te identifique!')
                            ])
