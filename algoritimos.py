import numpy as np
#As anotações são baseadas na disciplina de algoritimos do CIn-UFPE do curso de SI

#DEFINIÇÃO: um algoritmo é uma sequência de passos computacionais que transformam a ENTRADA na SAÍDA. 
#Também podemos visualizar um aigoritmo como uma ferramenta para resolver umproblema computacional bem especificado

# Objetivo da aula: Apresentar os conceitos de Vetores, Matrizes e Tensores, ilustrando-os em Python utilizando a biblioteca numpy.
"""
Em Python, listas são estruturas nativas que permitem o armazenamento sequencial de diversos valores. Mas em alguns contextos elas são ineficientes. 
Vetores, matrizes e tensores são alternativas a listas para armazenamento de múltiplos valores de mesmo tipo (estruturas homogêneas)
Os dados são armazenados de forma contígua na memória (endereços sequenciais para blocos de mesmo tamanho), permitem indexar os elementos de forma direta (o que é mais eficiente de que em listas)
"""

# ----------------------------------------------------VETORES ---------------------------------------------------------------------------------------------

# Vetores são estruturas UNIDIMENSIONAIS que armazenam elementos de um mesmo tipo.
# Numpy oferece suporte a vetores em Python encapsulando-os em objetos da classe "ndarray" (signidica numero dimensão array, ou. um array multidimensional)


# Como os dados são armazenados contiguamente, é preciso informar o tipo dos dados a ser guardado e sua quantidade.
"""
Usando a função "empty", é criado um vetor com espaços vazios. 

vetor = numpy.empty(shape, dtype=float, order='C')

shape: Especifica o tamanho e a forma do array que você deseja criar, como o número de linhas e colunas em um array bidimensional. Pode ser passado um número ou uma tupla (n, n)
dtype: Define o tipo de dado dos elementos no array, como inteiros, números de ponto flutuante, strings, etc.
order: Determina a ordem de armazenamento dos elementos na memória, podendo ser 'C' (ordem de C) para armazenamento por linhas ou 'F' (ordem de Fortran) para armazenamento por colunas.
"""

def vetor_empty():
    vetor_unidimensional = np.empty((4), int)
    print(f'Vetor unidimensional:\n {vetor_unidimensional}') # a sáida foi: [ 1747752668 -1627480792 -1602070744 -1923164309] (é lixo de memória)
    vetor_bidimensional = np.empty((2, 2), int)
    print(f'Vetor bidimensional:\n {vetor_bidimensional}')
# vetor_empty()



#-------------------------------------ATIVIDADES DO PDF---------------------------------------

# QUESTÕES PARA VETORES

"""Q1 - Construa um programa que preenche um vetor de inteiros de 100 números, colocando 0 nas posições pares e 1 nas ímpares."""
def questao_1_vetores():
    contador = 0
    vetor = np.ones((1, 100))
    for posicao in vetor[0]:
        if contador % 2 == 0:
            vetor[0][contador] = 0
        contador +=1
    print(vetor)

"""Q2 - Construa um programa que lê, soma e imprime o resultado da soma de um vetor de inteiros de 10 posições."""
def questao_2_vetores():
    vetor = np.linspace(1, 100, num=10, endpoint=True) # Lembrar que o primeiro parâmetro e inclusivo e o segundo é exclusivo!
    soma = np.sum(vetor)
    print(f'Soma: {soma}')

"""Q3 - Construa um programa que multiplique os valores de um vetor de reais de 20 posições pelos valores de um outro vetor de reais de 20 posições. O
primeiro vetor deve ser inicializado com valores crescentes a partir de 1 e o segundo vetor com valores decrescentes a partir de 20. Os resultados das
multiplicações devem ser armazenados num terceiro vetor."""
def questao_3_vetores():
    vetor_crescente = np.linspace(1, 20, num=20, endpoint=True) # Cria um vetor crescente
    vetor_decrescente = np.sort(vetor_crescente, kind='heapsort')# A partir do crescente, cria-se o decrescente
    produto_escalar = np.dot(vetor_crescente, vetor_decrescente)# Faz o PRODUTO ESCALAR dos dois vetores
    print(produto_escalar)

"""Q4 - Leia um vetor de 16 posições e troque os 8 primeiros valores pelos 8 últimos e vice-versa. Escreva ao final o vetor obtido."""
def questao_4_vetores():
    vetor = np.linspace(1, 16, num=16, endpoint=True) # Lembrar que o primeiro parâmetro e inclusivo e o segundo é exclusivo!
    print(vetor)
    primeira_metade = vetor[0: int((len(vetor)/2))]#Quebra o vetor na metade
    segunda_metade = vetor[int((len(vetor)/2)): ]#Quebra o vetor na metade
    print(primeira_metade)
    print(segunda_metade)
    #print((len(vetor)/2))
    vetor = np.array([])
    resultado = np.concatenate((segunda_metade, primeira_metade), axis=0)
    print(resultado)

# QUESTÕES PARA MATRIZES

"""Q1 - Construa um algoritmo que efetue e apresente o resultado da soma entre duas matrizes 3 x 5. Inicialize a matriz com valores quaisquer e imprima o resultado na tela."""
def questao_1_matrizes():
    contador = 0
    # CONDIÇÃO: As matrizes devem ser n x k
    # Dada as matrizes A + B = C, A[linha][coluna] + B[linha][coluna] = C[linha][coluna]
    matriz_1 = np.ones((3 ,5), dtype=float)
    dimensoes = matriz_1.shape
    print(f'Matriz 1: \n{matriz_1}')
    matriz_2 = np.ones((3 ,5), dtype=int)
    matriz_reposta = np.empty((dimensoes[0], dimensoes[1]), dtype=float)
    array_para_append = np.array([])
    print(f'Matriz 2: \n{matriz_2}\n')
    #RESOLUÇÃO: faz a soma escalar das linhas da matriz
    for linha_matriz_1, linha_matriz_2 in zip(matriz_1, matriz_2): # laço com as 2 matrizes
        for elemento_linha_matriz_1, elemento_linha_matriz_2 in zip(linha_matriz_1, linha_matriz_2):
            soma_elementos = elemento_linha_matriz_1 + elemento_linha_matriz_2
            array_para_append = np.append(array_para_append, soma_elementos)
            print(f'{elemento_linha_matriz_1} + {elemento_linha_matriz_2} = {soma_elementos}')
        matriz_reposta[contador] = array_para_append
        array_para_append = np.array([])
        contador += 1
    print(matriz_reposta)

"""Q2 - Faça um programa que multiplica uma matriz 3 x 3 de inteiros por um escalar k e imprima o resultado na tela. O usuário deve fornecer os valores da matriz e de k."""



"""Leia uma matriz 20 x 20. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final escrever a localização (linha e coluna) ou uma mensagem de “não 
encontrado”."""



"""Q4 - Leia um vetor de 16 posições e troque os 8 primeiros valores pelos 8 últimos e vice-versa. Escreva ao final o vetor obtido."""









#--------------------------------------------ANÁLISE DE ALGORITIMOS---------------------------------------------------------------------------------------------
