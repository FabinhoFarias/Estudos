import numpy as np

"""Q1 - Construa um algoritmo que efetue e apresente o resultado da soma entre duas matrizes 3 x 5. Inicialize a matriz com valores quaisquer e imprima o resultado na tela."""
def questao_1_matrizes():
    # CONDIÇÃO: As matrizes devem ser n x k
    # Dada as matrizes A + B = C, A[linha][coluna] + B[linha][coluna] = C[linha][coluna]
    matriz_1 = np.ones((3 ,5), dtype=int)
    print(f'Matriz 1: \n{matriz_1}')
    matriz_2 = np.ones((3 ,5), dtype=int)
    print(f'Matriz 2: \n{matriz_2}')
    #RESOLUÇÃO: faz a soma escalar das linhas da matriz
    #for i in matriz_1:

questao_1_matrizes()
