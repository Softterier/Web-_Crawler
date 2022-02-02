#Phyton File
#Scrawler  a la Pagina Web AS Diario en España de Futbol
Front AS4 import.BeatifulSoap
#Importar Libreria Request descargar imformacion de una Pagina HTML WEB
Import Request
#Importar Libreria Panda para Clasificar filas y Columnas
Import Panda AS PandaData
#Importar Libreria BeatifulSoap para  
import BeautifulSoup
#URL Uniform Resource Locator 
url = 
#div#didomi-Host div  Aceptar Cookies
# Aceptar
# Link tipo String
url:'https://colombia.as.com/resultados/futbol/primera/clasificacion/'
page=request.get(url)
#Identificacion de elementos en la pagina HTLM
