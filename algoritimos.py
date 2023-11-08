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

"""Q1 - Construa um programa que preenche um vetor de inteiros de 100 números, colocando 0 nas posições pares e 1 nas ímpares."""
def questao_1():
    contador = 0
    vetor = np.ones((1, 100))
    for posicao in vetor[0]:
        if contador % 2 == 0:
            vetor[0][contador] = 0
        contador +=1
    print(vetor)
"""Q2 - Construa um programa que lê, soma e imprime o resultado da soma de um vetor de inteiros de 10 posições."""
def questao_2():
    vetor = np.linspace(0, 100, num=10)
    soma = np.sum(vetor)
    print(soma)




























#--------------------------------------------ANÁLISE DE ALGORITIMOS---------------------------------------------------------------------------------------------
