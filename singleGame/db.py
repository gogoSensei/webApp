#!/usr/bin/env python
#-*- coding: utf-8 -*-

import MySQLdb 

DB_HOST = 'localhost' 
DB_USER = 'isidro' 
DB_PASS = 'kmotin818' 
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