import numpy as np

def questão_3_matrizes():
    numero_de_linhas = 0
    numero_de_colunas = 0
    matriz = np.random.randint(1, 401, size=(20,20))
    elemento_busca = float(input(f'Float: '))
    matriz_ordenada = np.sort(matriz)
    print(f'{matriz}\n\n{matriz_ordenada}')
    indices = np.where(matriz_ordenada == elemento_busca)
    print(indices)
questão_3_matrizes()
