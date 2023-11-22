import numpy as np
import pandas as pd


a = '28 33 27 30 31 30 33 30 33 29 27 33 31 27 31 28 27 29 31 24 31 33 30 32 30 33 27 33 31 33 23 29 30 24 28 34 30 30 18 17 18 15 16 17 17 18 19 19 20 29'
nada = a.split(' ')
arr = []
for i in nada:
    arr.append(int(i))
arr.sort()
print(arr)
arr = np.array(arr)
mediana = np.median(arr)
soma = np.sum(arr)
media = soma/len(arr)
qua1 = np.percentile(arr, 25.0)
qua3 = np.percentile(arr, 75.0)
p60 = np.percentile(arr, 60.0)
largura_classe = 19/6
cont =0
classes = []
for i in range(6):
    cont += largura_classe
    classes.append([])
    for j in arr:
        if min(arr)+cont-largura_classe <j and j<min(arr)+cont:
            classes[i].append(j)
            

print(classes)


print(f'Mediana: {mediana}')
print(f'media: {media}')
print(f'q1: {qua1}')
print(f'q3: {qua3}')
print(f'p60: {p60}')
