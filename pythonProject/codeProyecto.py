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
import os
import urllib.request
from io import BytesIO
import time
#--------------------------------------------------------------------
# -------------------------- FUNCIONES ------------------------------

def Presentación():
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
  time.sleep(5)

def mapearMascara(val):
  if val == 0:
    return 255
  else:
    return val

def datosUser():
  name = soup.find('div',{'class':'grid--cell fw-bold'}).text
  present = [ [ f'USUARIO ENCONTRADO - URL\n {URL}' ] ]
  userName = [[f'Nombre del Usuario: {name} \n ID: {userIdent}']]
  print(tabulate(present, tablefmt='fancy_grid', stralign='center'))
  print(tabulate(userName, tablefmt='fancy_grid', stralign='center')+ '\n')

def buscarEtiquetas():
  pagination = soupTag.find_all('a', class_='s-pagination--item js-pagination-item')
  if (len(pagination) == 0):
    ultimaPag = 1
  else:
    ultimaPag = int(pagination[-2].text)
  paginaEtiquetas = URL + '?tab=tags&sort=votes&page='
  iterator = 1
  while iterator <= ultimaPag:
    numPaginas = str(iterator)
    mostrarTags = requests.get(paginaEtiquetas + numPaginas)
    soupMostrar = BeautifulSoup(mostrarTags.content, 'html.parser')
    for row in soupMostrar.findAll('table')[0].tbody.findAll('td'):
      vte = row.findAll('div', class_='answer-votes')[0]
      ttb = row.findAll('a', class_='post-tag')[0]
      try:
        vte2 = int(vte.text)
        validarNumero = True
      except Exception as e:
        vte2 = vte.text
        validarNumero = False
      if (validarNumero == False):
        ch = int(vte2[ 0 ])
        ch *= 1000
        vte2 = int(vte2.replace(vte2, f'{ch}'))
      if vte2 > 0:
        listaVotos.append(vte2)
        listaTags.append(ttb.text)
    iterator += 1

def mostrarEtiquetas():
  m3 = []
  listaVtsModified = [iter(listaVotos)] * 4
  Matriz1 = list(zip_longest(*listaVtsModified, fillvalue=' '))
  listTagsModified = [iter(listaTags)] * 4
  Matriz2 = list(zip_longest(*listTagsModified, fillvalue=' '))
  print()
  ck = [ 'PUNTUACIONES  ETIQUETAS']
  print(tabulate(ck, tablefmt='plain', stralign='center')+'\n')
  for i in range((int(len(listaVotos) / 4))):
    m3.append([])
    for j in range(4):
      m3[i].append(f'{(Matriz1[i][j])}'+ ' : ' + str(Matriz2[i][j]))
  print(tabulate(m3,tablefmt='fancy_grid',stralign='center'))


def generarNube():
  maxWords = len(listaVotos)
  dic = dict(zip(listaTags, listaVotos))
  url2 = 'http://clipart-library.com/new_gallery/336-3364458_cloud-animation-png-clipart-png-download-cloud-animation.png'
  response = requests.get(url2)
  cd = Image.open(BytesIO(response.content))
  cloudPNG = np.array(cd)
  maskCloud = np.ndarray((cloudPNG.shape[ 0 ], cloudPNG.shape[ 1 ]), np.int32)
  for i in range(len(cloudPNG)):
    maskCloud[ i ] = list(map(mapearMascara, cloudPNG[ i ]))
  wc = WordCloud(background_color='white', max_words = maxWords, mask=maskCloud, colormap = 'Blues').generate_from_frequencies(dic)
  plt.figure(figsize=[ 20, 10 ])
  plt.imshow(wc, interpolation='bilinear')
  plt.axis("off")
  plt.show()
#-----------------------------------------------------------------------

 # ------------- MAIN --------------------------------------------------
Presentación()
try:
  try :
      userid = input('Ingrese el ID del usuario: ')
      entrada = int(userid)
      if entrada > 0:
          userIdent = str(userid)
          listaVotos = list()
          listaTags = list()
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
                      while opcion != 0:                       
                        if opcion == 1:
                          mostrarEtiquetas()
                        if opcion == 2:
                          generarNube()
                        opcion = int(input('\n 1: Ver etiquetas \n 2: Ver nube de etiquetas \n 0: salir \n OPCION: '))
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
