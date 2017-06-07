#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Se requiere instalar primero pymysql para utilizar el conector 
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb 

DB_HOST = 'localhost' 
DB_USER = 'jose' #'isidro' 
DB_PASS = 'MUSEMUSE' #'kmotin818' 
DB_NAME = 'easygame' 
datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
"""docstring for DBase"""
def run_query(query):
	try:
   	    conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
   	    cursor = conn.cursor()         # Crear un cursor 
   	    cursor.execute(query)          # Ejecutar una consulta 
   	    if query.upper().startswith('SELECT'): 
   	        data = cursor.fetchall()   # Traer los resultados de un select 
   	    else: 
   	        conn.commit()              # Hacer efectiva la escritura de datos 
   	        data = None 
   	    cursor.close()                 # Cerrar el cursor 
   	    conn.close()                   # Cerrar la conexión 
   	    return data
	except Exception as e:
		print(e)
	else:
		print("Error desconocido")

"""
Para conectarse a mysql
mysql -u jose -p

Inicio de la base
CREATE DATABASE easygame ;
USE easygame;

tabla de pruebas
CREATE TABLE directorio (nombre TEXT, correo TEXT, descripcion TEXT);

insert de mentis
INSERT INTO directorio VALUES ('joemag','greengamboa@gmail.com','hola prro');
"""