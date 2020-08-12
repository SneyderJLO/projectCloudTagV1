import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

def transform_format(val):
    if val == 0:
        return 255
    else:
        return val

my_list=["one", "one two", "three"]
stopwords = set(STOPWORDS)
wine_mask = np.array(Image.open("mask.png"))
print(wine_mask)

transformed_wine_mask = np.ndarray((wine_mask.shape[0],wine_mask.shape[1]), np.int32)


for i in range(len(wine_mask)):
    transformed_wine_mask[i] = list(map(transform_format, wine_mask[i]))
wc = WordCloud(background_color='white', max_words=1000, mask=transformed_wine_mask, stopwords=stopwords,
                       contour_width=3, contour_color='white')


