
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from urllib.request import Request
from tabulate import tabulate
from itertools import  zip_longest
import requests
import urllib.request

def transform_format(val):
    if val == 0:
        return 255
    else:
        return val

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
                listaTags += ttb
        iterator += 1

    '''if len(listaVotos) != 0:
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
        stopwords = set(STOPWORDS)
        wine_mask = np.array(Image.open("84419.png"))
        transformed_wine_mask = np.ndarray((wine_mask.shape[ 0 ], wine_mask.shape[ 1 ]), np.int32)

        for i in range(len(wine_mask)) :
            transformed_wine_mask[ i ] = list(map(transform_format, wine_mask[ i ]))

        wc = WordCloud(background_color='white', max_words=1000, mask=transformed_wine_mask, stopwords=stopwords,
                       contour_width=3, contour_color='dimgray')

        text = " ".join(listaTags)
        wc.generate(text)

        wc.to_file("cat2.png")
        plt.figure(figsize=[ 20, 10 ])
        plt.imshow(wc, interpolation='bilinear')
        plt.axis("off")
        plt.show()
    else:
        print('El usuario dispone de etiquetas, pero no posee puntuaciones.')'''




try :
    userid = input('Ingrese el ID del usuario: ')
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
except ValueError :
    print('Solo ingrese dígitos enteros')
