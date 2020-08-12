from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from collections import Counter
from bs4 import BeautifulSoup
import numpy as np
from urllib.request import Request
from itertools import  zip_longest

from pip._internal.utils.misc import tabulate
from scrapy.item import Field, Item
import requests
import lxml.html
from scrapy.loader import ItemLoader
import urllib.request

'''
requ = urllib.request.Request(url=URL)
with urllib.request.urlopen(requ) as f:
    x = f.read()
print(x)
'''



def datosUser():
    name = soup.find_all('div', class_='grid--cell fw-bold')
    print('Id: ' + userIdent)
    for i in name:
        print('Nombre User: ' + i.text)


def buscarEtiquetas():
    n = 1

    pagination = soupTag.find_all('a', class_='s-pagination--item js-pagination-item')
    valuePag = list()
    for i in pagination:
        valuePag.append(i.text)
    if (len(valuePag) == 0):
        ultimaPag = 1
    else:
        ultimaPag = int(valuePag[-2])
    # print(valuePag)
    # print(ultimaPag)

    paginaEtiquetas = URL + '?tab=tags&sort=votes&page='
    iterator = 1
    matriz = []
    index = 0
    contadorTags = 1
    listaTags = list()
    listaVotos = list()

    while iterator <= ultimaPag:
        numPaginas = str(iterator)
        mostrarTags = requests.get(paginaEtiquetas + numPaginas)
        soupMostrar = BeautifulSoup(mostrarTags.content, 'html.parser')
        votos = soupMostrar.findAll('div', class_='answer-votes')
        alltags = soupMostrar.find_all('a', class_='post-tag')
        tr = soupMostrar.findAll('tr')
        td = soupMostrar.findAll('td')
        alltag2s = soupMostrar.find_all('a', class_='post-tag')
        for row in soupMostrar.findAll('table')[0].tbody.findAll('td'):
                listaVotos += row.findAll('div', class_='answer-votes')[0].contents
                listaTags += row.findAll('a', class_='post-tag')[0].contents

         #para terminar el bucle
        iterator += 1
    print('-PUNTUACIÓN | ETIQUETAS------')
    union = list(zip(listaVotos, listaTags))
    args = [ iter(union) ]*1
    M = list(zip_longest(*args))
    #arrays = np.array(M)
    print(union)




    '''union = tuple(zip(listaVotos, listaTags))'''


userid = int(input('ingrese id '))  # user ingresa id
userIdent = str(userid)
print((userIdent))
URL = 'https://es.stackoverflow.com/users/' + userIdent  # concatenar cadenas
# print(URL)
pagina = requests.get(URL)
pagTab = requests.get(URL + '?tab=tags&sort=votes&page=1')
soup = BeautifulSoup(pagina.content, 'html.parser')
soupTag = BeautifulSoup(pagTab.content, 'html.parser')

try:
    fhand = urllib.request.urlopen(URL).read().decode()  # obtener el codigo para validar si el usuario existe
    validar = bool(fhand)
    if validar == True:
        print('USER ENCONTRADO - URL: ' + URL)
        datosUser()
        buscarEtiquetas()
        # llenarEtiquetas()
except Exception as e:
    print('No hay datos para mostrar')

