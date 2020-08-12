'''from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from scrapy.item import Field, Item
import requests
from scrapy.loader import ItemLoader
import urllib.request


requ = urllib.request.Request(url=URL)
with urllib.request.urlopen(requ) as f:
    x = f.read()
print(x)



def datosUser():
    name = soup.find_all('div', class_='grid--cell fw-bold')
    print('Id: ' + userIdent)
    for i in name:
        print('Nombre User: ' + i.text)


def buscarEtiquetas():
    pagination = soupTag.find_all('a', class_='s-pagination--item js-pagination-item')
    valuePag = list()
    for i in pagination:
        valuePag.append(i.text)
    ultimaPag = int(valuePag[-2])
    print(ultimaPag)


    x = 1
    while x <= ultimaPag:
        mostrarTags = requests.get(URL+ '?tab=tags&sort=votes&page='+x)
        soupMostrar = BeautifulSoup(mostrarTags.content, 'html.parser')
        tags = soupMostrar.find_all('a', class_='post-tag')
        allTags = list()
        x += 1
        for m in tags:
            allTags.append(i.text)
            print(allTags)


for a in tags:
            allTags.append(a.text)
        #print(allTags,len(allTags))

        unicos = []
        allTagsCopy = list(allTags)
        for n in allTagsCopy:
                if n not in unicos:
                    unicos.append(n)
                else:
                    allTags.remove(n)

        print(unicos,len(unicos))


userid = int(input('ingrese id '))  # user ingresa id
userIdent = str(userid)
print((userIdent))
URL = 'https://es.stackoverflow.com/users/' + userIdent  # concatenar cadenas
print(URL)
pagina = requests.get(URL)
pagina+='?tab=tags'
pagTab = requests.get(pagina)
soup = BeautifulSoup(pagina.content, 'html.parser')
soupTag = BeautifulSoup(pagTab.content, 'html.parser')

try:
    fhand = urllib.request.urlopen(URL).read().decode()  # obtener el codigo para validar si el usuario existe
    validar = bool(fhand)
    if validar == True:
        print('encontrado')
        datosUser()
        buscarEtiquetas()

except Exception as e:
    print('User No encontrado')

def buscarName(x):
    item = ItemLoader(x)
    item.add_xpath('//*[@id="user-card"]/div/div[2]/div/div[1]/div/div[1]/h2/div/text()')
    yield item.load_item()


def llenarEtiquetas():

    paginaEtiquetas = URL+'?tab=tags&sort=votes&page='
   # soupTag = BeautifulSoup(paginaEtiquetas.content, 'html.parser')
    xe = 1
    while xe <= 5:
        ye = str(xe)
        mostrarTags = requests.get(paginaEtiquetas+ye)
        soupMostrar = BeautifulSoup(mostrarTags.content, 'html.parser')
        tags = soupMostrar.find_all('a', class_='post-tag')
        xe = xe + 1
        allTags = list()
        for m in tags:
            print(m.text)
                #allTags.append(m.text)
                #print(allTags)
    xe = xe+1




'''


#print(len(td))

        '''for f in range(4):
            for c in range(len(td)):
                userTags = soupMostrar.select(f'#user-tab-tags > div.user-tab-content > table > tbody > tr:nth-child({c}) > td:nth-child({f}) > a')

                print(userTags)'''


                    #listaTags.append(userTags)

                #print(listaTags)

        '''for i in votos:
                listaVotos.append(i.text)'''




        #for i in len(Alltags):
            #posicionElemento = str(i)
            #userTags = soupMostrar.select(f"#user-tab-tags > div.user-tab-content > table > tbody > tr:nth-child({n}) > td:nth-child({n}) > a")

            #userTags = soupMostrar.select('#user-tab-tags > div.user-tab-content > table > tbody > tr:nth-child('+numPaginas+')'+'> td:nth-child('+posicionElemento+') > div')



        #tags = soupMostrar.select('#user-tab-tags > div.user-tab-content > table > tbody > tr:nth-child(4) > td:nth-child(1) > div')


'''for i in tags:

            if m not in allTags:
                allTags.append(i.text)
            else:
                del allTags[i]

        print('---------etiquetas-----------')
        #print(m)
        print(allTags, len(allTags))
        print('------------------------------')'''

'''counTag = soupMostrar.find_all('td')
    print(len(counTag))

    iterator = iterator + 1

    tags = soupMostrar.find_all('a', class_='post-tag')
    puntuacion = soupMostrar.find_all('div', class_='answer-votes')
    allTags = list()
    count = 0'''
'''for a in puntuacion:
            print(a.text)'''
'''for m in tags:
        if count < counTag:
            allTags.append(m.text)
        else:
            break
        count += 1
    print(allTags, len(allTags))'''
# print(m.text)
# allTags.append (m.text)
# print(allTags)

# print(len(counTag))
'''x = 1
while x < 3:

    mostrarTags = requests.get(pagTab+'1')
    soupMostrar = BeautifulSoup(mostrarTags.content, 'html.parser')
    tags = soupMostrar.find_all('a', class_='post-tag')
    allTags = list()
    for m in tags:
        allTags.append(''+m.text)
        print(allTags)

x+=1'''

def llenarEtiquetas():

    paginaEtiquetas = URL+'?tab=tags&sort=votes&page='
   # soupTag = BeautifulSoup(paginaEtiquetas.content, 'html.parser')
    xe = 1
    while xe <= 5:
        ye = str(xe)
        mostrarTags = requests.get(paginaEtiquetas+ye)
        soupMostrar = BeautifulSoup(mostrarTags.content, 'html.parser')
        tags = soupMostrar.find_all('a', class_='post-tag')
        allTags = list()
        for m in tags:
            print(m.text)
                #allTags.append(m.text)
                #print(allTags)
    xe = xe+1