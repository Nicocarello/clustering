# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:20:51 2020

@author: Usuario
"""

from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram,linkage
import pandas as pd


data = pd.read_csv('D:/Anaconda/datasets/movies/movies.csv',sep=';')

#AGARRO LAS PELICULAS EN UNA LISTA
movies = data.columns.values.tolist()[1:]

#HAGO TODOS LOS ENLACES DEL DATAFRAME
z = linkage(data[movies],'average')

print(z)

plt.figure(figsize=(25,10))
plt.title('Dendograma jerarquico para clustering')
plt.xlabel('ID de los usuarios de Netflix')
plt.ylabel('Distancia')
dendrogram(z,leaf_rotation=90,leaf_font_size=10)
plt.show()