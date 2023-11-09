import numpy as np

def questao_1_matrizes():
    matriz = np.ones((3 ,3), dtype=int)
    numero_de_lihas = 0
    numero_de_colunas = 0
    for linha in matriz:
        numero_de_lihas += 1
        for elemento in linha:
            numero_de_colunas += 1
            elemento = int(input(f'A{numero_de_lihas}{numero_de_colunas}: '))
        numero_de_colunas = 0
        
        
    K = int(input('Constante: '))
    #dimensoes = matriz_1.shape
    print(f'Matriz: \n{matriz}')
    #matriz_reposta = np.empty((dimensoes[0], dimensoes[1]), dtype=float)
    #RESOLUÇÃO: faz a soma escalar das linhas da matriz
    for linha in matriz:
        numero_de_lihas += 1
        for elemento in linha:
            numero_de_colunas += 1
            elemento = int(input(f'A{numero_de_lihas}{numero_de_colunas}: '))
        numero_de_colunas = 0
    #print(matriz_reposta)
questao_1_matrizes()
