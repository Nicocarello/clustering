#CALCULAR LAS DISTANCIAS MATRIZ

from scipy.spatial import distance_matrix

import pandas as pd

data = pd.read_csv('D:/Anaconda/datasets/movies/movies.csv',sep=';')

#AGARRO LAS PELICULAS EN UNA LISTA
movies = data.columns.values.tolist()[1:]

dd1 = distance_matrix(data[movies],data[movies],p=1)
dd2 = distance_matrix(data[movies],data[movies],p=2)
dd10 = distance_matrix(data[movies],data[movies],p=10)

#PASO LAS LISTAS CON LAS DISTANCIAS A UN DATAFRAME

def dm_to_df(dd,col_name):
    import pandas as pd
    return pd.DataFrame(dd,index=col_name,columns=col_name)

dd1 = dm_to_df(dd1,data['user_id'])
dd2 = dm_to_df(dd2,data['user_id'])
dd10 = dm_to_df(dd10,data['user_id'])

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()

ax= fig.add_subplot(111,projection='3d')
ax.scatter(xs= data['star_wars'],ys=data['lord_of_the_rings'],zs=data['harry_potter'])

###ENLACES

df = dd1

z=[]

#CALCULAR LA DISTANCIA MAS PEQUEÑA

df[11] = df[1]+df[10]
df.loc[11]= df.loc[1]+df.loc[10]
z.append([1,10,0.7,2])

#REEMPLAZO VALORES DE FILA 11 CON LOS MINIMOS DE LA 1 A LA 10

for i in df.columns.values.tolist():
    df.loc[11][i]=min(df.loc[1][i],df.loc[10][i])
    df.loc[i][11]=min(df.loc[i][1],df.loc[i][10])

df= df.drop([1,10])
df= df.drop([1,10],axis=1)
