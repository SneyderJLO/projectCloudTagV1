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

userid = int(input('ingrese id '))  # user ingresa id
userIdent = str(userid)
print((userIdent))
URL = 'https://es.stackoverflow.com/users/' + userIdent  # concatenar cadenas
# print(URL)
pagina = requests.get(URL)
pagTab = requests.get(URL + '?tab=tags&sort=votes&page=1')
soup = BeautifulSoup(pagina.content, 'html.parser')
soupTag = BeautifulSoup(pagTab.content, 'html.parser')

fhand = urllib.request.urlopen(URL).read().decode()  # obtener el codigo para validar si el usuario existe


