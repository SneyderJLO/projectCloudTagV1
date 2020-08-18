#------------------------ LIBRERÍAS --------------------------------
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from urllib.request import Request
from tabulate import tabulate
from itertools import  zip_longest
import requests
import urllib.request
from io import BytesIO
import time
import os
from IPython.display import clear_output
#--------------------------------------------------------------------
# -------------------------- FUNCIONES ------------------------------
def Presentacion():
  print(" _____         _                                     _                 ")
  print("|_   _|       | |                                   | |              _ ")
  print("  | |   _ __  | |_   ___   __ _  _ __   __ _  _ __  | |_   ___  ___ (_)")
  print("  | |  | '_ \ | __| / _ \ / _` || '__| / _` || '_ \ | __| / _ \/ __|   ")
  print(" _| |_ | | | || |_ |  __/| (_| || |   | (_| || | | || |_ |  __/\__ \ _ ")
  print(" \___/ |_| |_| \__| \___| \__, ||_|    \__,_||_| |_| \__| \___||___/(_)")
  print("                           __/ |                                       ")
  print("                          |___/                                        ")
  print("  _       _               _                      ___                   _        ")
  print(" / |     /_\    _ _    __| |  _ _   ___   ___   | _ \  _ _   __ _   __| |  ___  ")
  print(" | | _  / _ \  | ' \  / _` | | '_| / -_) (_-<   |  _/ | '_| / _` | / _` | / _ \ ")
  print(" |_|(_)/_/ \_\ |_||_| \__,_| |_|   \___| /__/   |_|   |_|   \__,_| \__,_| \___/ ")
  print(" ___        _                       _     _                      ___          _      ")
  print("|_  )    _ | |  ___   _ _    __ _  | |_  | |_    __ _   _ _     | _ \  _  _  (_)  ___")
  print(" / /  _ | || | / _ \ | ' \  / _` | |  _| | ' \  / _` | | ' \    |   / | || | | | |_ /")
  print("/___|(_) \__/  \___/ |_||_| \__,_|  \__| |_||_| \__,_| |_||_|   |_|_\  \_,_| |_| /__|")
  print(" ____    _  _                                        _____                                         ")
  print("|__ /   | \| |  ___   _  _   ___  ___  ___   _ _    |_   _|  ___   _ _    ___   _ __    ___   __ _ ")
  print(" |_ \ _ | .` | / -_) | || | (_-< (_-< / -_) | '_|     | |   / -_) | ' \  / -_) | '  \  / -_) / _` |")
  print("|___/(_)|_|\_| \___|  \_, | /__/ /__/ \___| |_|       |_|   \___| |_||_| \___| |_|_|_| \___| \__,_|")
  print("                        |__/                                                                         ")
  time.sleep(7)
  clear_output()

def installFont():
  if os.path.isfile('bankgthd.ttf'):
    print('')
  else:
    !wget https://www.fontsupply.com//fonts/bankgthd.ttf
    clear_output()

def mapearMascara(val): #para poder generar una wordcloud se necesita una mask con valores 255 en todo el array, hay unas que varían de 0 a 1
  if val == 0: 
    return 255 # cambiamos el valor de 0 a 255
  else:
    return val

def datosUser():
  name = soup.find('div',{'class':'grid--cell fw-bold'}).text #se halla el contenido por clase name
  names.append(name)
  present = [ [ f'USUARIO ENCONTRADO - URL\n {URL}' ] ]
  userName = [[f'Nombre del Usuario: {name} \n ID: {userIdent}']]
  print(tabulate(present, tablefmt='fancy_grid', stralign='center')) #fancy_grid es el estilo de tabla predefinifido por el table
  print(tabulate(userName, tablefmt='fancy_grid', stralign='center')+ '\n')

def buscarEtiquetas():
  pagination = soupTag.find_all('a', class_='s-pagination--item js-pagination-item') #se busca la cantidad de páginas que hay para las etiquetas
  if (len(pagination) == 0): #se valida si hay mínimo una página por etiqueta
    ultimaPag = 1
  else:
    ultimaPag = int(pagination[-2].text) #dado que el último elemento es: Siguiente, con [-2] retrocede a la posición que contiene un número(último elemento de la lista)
  paginaEtiquetas = URL + '?tab=tags&sort=votes&page=' #se concatena la url con la página designada para las etiquetas
  iterator = 1
  while iterator <= ultimaPag: 
    numPaginas = str(iterator)
    mostrarTags = requests.get(paginaEtiquetas + numPaginas)
    soupMostrar = BeautifulSoup(mostrarTags.content, 'html.parser')
    for row in soupMostrar.findAll('table')[0].tbody.findAll('td'): #se detiene cuando encuentra la primera tabla y todos los subcampos 'td'
      vte = row.findAll('div', class_='answer-votes')[0] #busca el campo donde haya la puntuación de cada etiqueta
      ttb = row.findAll('a', class_='post-tag')[0] # busca el campo donde haya la etiqueta por tabla
      try: #se valida si la puntuaciòn es número o string
        vte2 = int(vte.text) #se convierte a entero cada elemento puntuación
        validarNumero = True
      except Exception as e:
        vte2 = vte.text
        validarNumero = False
      if (validarNumero == False):
        ch = int(vte2[ 0 ])
        ch *= 1000
        vte2 = int(vte2.replace(vte2, f'{ch}')) #se reemplaza el k por 1000
      if vte2 > 0: #se eliminan todas las puntuaciones y etiquetas que sean negativas o iguales a cero
        listaVotos.append(vte2)
        listaTags.append(ttb.text)
    iterator += 1

def mostrarEtiquetas():
  m3 = []
  listaVtsModified = [iter(listaVotos)] * 4 #se convierte la lista en filas y columnas
  Matriz1 = list(zip_longest(*listaVtsModified, fillvalue=' '))
  listTagsModified = [iter(listaTags)] * 4
  Matriz2 = list(zip_longest(*listTagsModified, fillvalue=' '))
  print()
  ck = [f'PUNTUACIONES  ETIQUETAS: {names[0]}']
  print(tabulate(ck, tablefmt='plain', stralign='center')+'\n')
  print(tabulate([[ f'Ver Usuario: {URL}'+'?tab=tags']],tablefmt='fancy_grid', stralign='center'))
  for i in range((int(len(listaVotos) / 4))):
    m3.append([])
    for j in range(4):
      m3[i].append(f'{(Matriz1[i][j])}'+ ' : ' + str(Matriz2[i][j])) #se añaden los elementos de cada lista a una matriz nueva
  print(tabulate(m3,tablefmt='fancy_grid',stralign='center')) #se presentan los elementos de la nueva matriz


def generarNube():
  maxWords = len(listaVotos) #se determina la cantidad de elmentos de la listaVotos(puntuaciones)
  dic = dict(zip(listaTags, listaVotos)) #se crea un diccionario donde cada etiqueta contiene su puntuacion
  url2 = 'https://image.flaticon.com/icons/png/512/23/23796.png' #url de la img para generar la máscara
  response = requests.get(url2)
  cd = Image.open(BytesIO(response.content))
  cloudPNG = np.array(cd) #convertir la img a array 
  maskCloud = np.ndarray((cloudPNG.shape[ 0 ], cloudPNG.shape[ 1 ]), np.int32) #se determinan solo los valores 0 y 1 para ser cambiados a 255
  for i in range(len(cloudPNG)):
    maskCloud[ i ] = list(map(mapearMascara, cloudPNG[ i ]))
  wc = WordCloud(font_path='bankgthd.ttf',  background_color='white', max_words = maxWords, mask=maskCloud).generate_from_frequencies(dic) #generar la nube de palabras
  plt.figure(figsize=[ 20,10]) #asignar el tamaño de la img
  userName = [[f'Nube de palabras del usuario: {names[0]}']]
  print(tabulate(userName, tablefmt='fancy_grid', stralign='center')+ '\n')
  plt.imshow(wc) #convertir la nube de palabras en objeto figura para ser presentada
  plt.axis("off") #oculta los bordes de la figura generada
  plt.show()#mostrar la figura resultante
#-----------------------------------------------------------------------

 # ------------- MAIN --------------------------------------------------

try:
  installFont()
  Presentacion() #se llama a la función Presentacion()
  try :
      userid = input('Ingrese el ID del usuario\n ')
      entrada = int(userid)
      if entrada > 0:
          userIdent = str(userid)
          listaVotos = list()
          listaTags = list()
          names = list()
          URL = 'https://es.stackoverflow.com/users/' + userIdent  # concatenar cadenas
          pagina = requests.get(URL)
          pagTab = requests.get(URL + '?tab=tags&sort=votes&page=1')
          soup = BeautifulSoup(pagina.content, 'html.parser')
          soupTag = BeautifulSoup(pagTab.content, 'html.parser')
          userValidation = soup.find_all('div', class_='grid--cell mb16 profile-placeholder--image')
          try:
              fhand = urllib.request.urlopen(URL+'?tab=tags')  # obtener el codigo para validar si el usuario existe
              if len(userValidation) == 1:
                  print('El usuario no cuenta con etiquetas')
              else:
                  datosUser()  
                  buscarEtiquetas()
                  if len(listaVotos) != 0:
                    try:
                      opcion = int(input('\n 1: Ver etiquetas \n 2: Ver nube de etiquetas \n 0: salir \n OPCION: '))
                      clear_output()
                      while opcion != 0:                       
                        if opcion == 1:
                          mostrarEtiquetas()
                        if opcion == 2:
                          generarNube()
                        opcion = int(input('\n 1: Ver etiquetas \n 2: Ver nube de etiquetas \n 0: salir \n OPCION: '))
                        clear_output()
                    except ValueError:
                      print('No válido, solo opción 1 | 2 | 0')
                  else:
                    print('El usuario tiene etiquetas, pero no posee puntuaciones.')
          except Exception as e:
              print('Error 404 - Página no encontrada')
  except ValueError :
      print('Solo ingrese dígitos enteros')
except KeyboardInterrupt:
  exit()
#--------------------------------------------------------------------------------------
