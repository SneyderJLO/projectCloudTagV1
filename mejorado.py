
import numpy as np

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request
from tabulate import tabulate
from itertools import  zip_longest
import requests
import urllib.request

def validaciones(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def datosUser():
    name = soup.find_all('div', class_='grid--cell fw-bold')
    c = name[0].text
    present = [ [ f'USUARIO ENCONTRADO - URL\n {URL}' ] ]
    userName = [[f'Nombre del Usuario: {c} \n ID: {userIdent}']]
    print(tabulate(present, tablefmt='fancy_grid', stralign='center'))
    print(tabulate(userName, tablefmt='fancy_grid', stralign='center'))
    print()
    print()
    #cmd.mkdir *da $


def buscarEtiquetas():
    pagination = soupTag.find_all('a', class_='s-pagination--item js-pagination-item')
    if (len(pagination) == 0):
        ultimaPag = 1
    else:
        ultimaPag = int(pagination[-2].text)

    paginaEtiquetas = URL + '?tab=tags&sort=votes&page='
    iterator = 1
    listaTags = list()
    listaVotos = list()
    while iterator <= ultimaPag:
        numPaginas = str(iterator)
        mostrarTags = requests.get(paginaEtiquetas + numPaginas)
        soupMostrar = BeautifulSoup(mostrarTags.content, 'html.parser')
        for row in soupMostrar.findAll('table')[0].tbody.findAll('td'):
            vte = row.findAll('div', class_='answer-votes')[0]
            ttb = row.findAll('a', class_='post-tag')[0]
            if ((vte.text=='0') or (vte.text=='-1') or (vte.text=='-2') )==False:
                listaVotos += vte
                listaTags += ttb
        iterator += 1
    if len(listaVotos) != 0:
        m3 = []
        listaVtsModified = [iter(listaVotos)] * 4
        Matriz1 = list(zip_longest(*listaVtsModified))
        listTagsModified = [iter(listaTags)] * 4
        Matriz2 = list(zip_longest(*listTagsModified))
        ck = [ '       PUNTUACIONES  ETIQUETAS' ]
        print(tabulate(ck, tablefmt='plain', stralign='center'))
        for i in range((int(len(listaVotos) / 4))):
            m3.append([])
            for j in range(4):
                m3[i].append(str(Matriz1[i][j])+ ' : ' +str(Matriz2[i][j]))
        print(tabulate(m3,tablefmt='fancy_grid',stralign='center'))
    else:
        print('El usuario dispone de etiquetas, pero no posee puntuaciones.')


while True:
    userid = input('Ingrese el ID del usuario: ')
    try :
        entrada = int(userid)
        if entrada > 0:
            userIdent = str(userid)
            URL = 'https://es.stackoverflow.com/users/' + userIdent  # concatenar cadenas
            pagina = requests.get(URL)
            pagTab = requests.get(URL + '?tab=tags&sort=votes&page=1')
            soup = BeautifulSoup(pagina.content, 'html.parser')
            soupTag = BeautifulSoup(pagTab.content, 'html.parser')
            userValidation = soup.find_all('div', class_='grid--cell mb16 profile-placeholder--image')
            try:
                fhand = urllib.request.urlopen(URL)  # obtener el codigo para validar si el usuario existe
                if len(userValidation) == 1:
                    print('El usuario no cuenta con etiquetas')
                else:
                    datosUser()

                    buscarEtiquetas()
            except Exception as e:
                print('Error 404 - Página no encontrada')
            
#esto es un comentario de andres prado xdd
    except ValueError :
        print('Solo ingrese dígitos enteros')
