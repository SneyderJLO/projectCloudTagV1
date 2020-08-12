from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from collections import Counter
from bs4 import BeautifulSoup
import numpy as np
from urllib.request import Request
from itertools import zip_longest

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


'''def datosUser():
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
    if (len(valuePag)==0):
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
    count = 0
    while iterator <= ultimaPag:
        numPaginas = str(iterator)
        mostrarTags = requests.get(paginaEtiquetas + numPaginas)
        soupMostrar = BeautifulSoup(mostrarTags.content, 'html.parser')
        votos = soupMostrar.findAll('div', class_='answer-votes')
        alltags = soupMostrar.find_all('a', class_='post-tag')
        tr = soupMostrar.findAll('tr')
        td = soupMostrar.findAll('td')
        alltag2s = soupMostrar.find_all('a', class_='post-tag')
        for k in td:
            eti = k.find('a')
            listaTags += eti
            vte = k.find('div')
            listaVotos += vte
            if vte.text == '0':
                count += 1

        iterator += 1
    print(listaVotos)
    r = 1
    print(len(listaTags))
    print(count)
    while r <= len(listaVotos)-count:
        if listaVotos[r] == '0':
            del listaTags[r]
        r += 1
    print(listaTags)
    print(len(listaTags))'''



'''userid = int(input('ingrese id '))  # user ingresa id
userIdent = str(userid)
print((userIdent))
URL = 'https://es.stackoverflow.com/users/' + userIdent  # concatenar cadenas
# print(URL)
pagina = requests.get(URL)
pagTab = requests.get(URL + '?tab=tags&sort=votes&page=1')
soup = BeautifulSoup(pagina.content, 'html.parser')
soupTag = BeautifulSoup(pagTab.content, 'html.parser')

userValidation = soup.find_all('div', class_='grid--cell mb16 profile-placeholder--image')
print(len(userValidation))
'''
'''for i in range(3):
    for j in range(3):
        b += str(M[i][j]) + '  ' +str(M2[i][j]) + '\t' + '  '
    print(b)'''


def lee_entero() :
    while True :
        entrada = input('Escribe un numeroentero: ')
        try :
            entrada = int(entrada)
            return entrada
        except ValueError:
            print('La entrada es incorrecta: escribe un numero entero')



b = ""
matrizx = [[111111111,22222,34341243],
          [414124,424125,24246],
          [7,812414,9]]
matriz1 = ['1','2','3','1','2','3','1','2','3','1','2','3','1','2','3','1','2','3','1','2','3','1','2','3','1','2','3']
args = [ iter(matriz1) ]*4
M = list(zip_longest(*args))
print(M)
matriz2 = ['1231','2232','3','1','2','3','1','2','3','1','2','3','1','2','3','1','2','3','1','2','3','1','2','3','1','2','3']
args2 = [ iter(matriz2) ]*4
M2 = list(zip_longest(*args2))
print(M2)


'''while True:
    entrada = input("Escribe un numero entero: ")
    try:
        sr = int(entrada)

    except ValueError:
        print ("La entrada es incorrecta: escribe un numero entero"'''

num = lee_entero()
print(type(num))


