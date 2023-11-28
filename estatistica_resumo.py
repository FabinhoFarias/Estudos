import numpy as np
import pandas as pd

def besteira():
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


#----------------------------------------ATIVIDADE-------------------------------------------
import time

def moda(lista):
    elemento = []
    frequencia = []
    for i in lista:
        if i not in elemento:
            elemento.append(i)
            frequencia.append(1)
        else:
            frequencia[-1] += 1
    frequencia_Max = max(frequencia)
    index = frequencia.index(frequencia_Max)
    moda_lista = elemento[index]
    print(f'Moda: {moda_lista}')

def mediana(lista):
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        mediana = (lista[n // 2 - 1] + lista[n // 2]) / 2
    else:
        mediana = lista[n // 2]
    print(f'Mediana: {mediana}')

def media_aritmetica(lista):
    soma = 0
    for i in lista:
        soma += i
    media = soma / len(lista)
    print(f'Média: {media}')

def tabela_de_frequencia(lista):
    elemento = []
    frequencia = []
    lista.sort()
    for i in lista:
        if i not in elemento:
            elemento.append(i)
            frequencia.append(1)
        else:
            frequencia[-1] += 1
    print('-----TABELA DE FREQUENCIA-----\n')
    for i in range(len(elemento)):
        print(f'---- {elemento[i]} --------------- {frequencia[i]} ----')
        time.sleep(0.3)

def quartil(n, lista):
    lista = np.array(lista)
    q = 0
    if n == 1:
        q = np.percentile(lista, 25)
        print(f'Primeiro quartil: {q}')
    if n == 2:
        q = np.percentile(lista, 50)
        print(f'Primeiro quartil: {q}')
    if n == 3:
        q = np.percentile(lista, 75)
        print(f'Primeiro quartil: {q}')
    if n == 4:
        q = np.percentile(lista, 100)
        print(f'Primeiro quartil: {q}')

def percentil(n, lista):
    lista = np.array(lista)
    q = np.percentile(lista, n)
    print(f'Percentil {n}: {q}')

def questao1():
    comando = '\nDescreva o que são dados quantitativos e qualitativos. Explique e dê três exemplos para cada um deles.\n'
    dados_quantitativos = 'Envolve quantidade de algo, ou seja, algo que pode ser medido ou mensurado!'
    exemplo_dado_quantitativo = '\nAceleração da gravidade; \nNumero de vendas de um carro A; \nNumero de memória em um conjunto de modelos de computador. \n'
    dados_qualitativos = 'Envolve uma informação que não pode ser mensurada'
    exemplo_dado_qualitativo = '\nCor de roupa; \nNome de pessoas; \nSatisfação de um restaurante. '
    print(comando.upper())
    time.sleep(0.5)
    print(f'DADOS QUANTITATIVOS:{dados_quantitativos}')
    time.sleep(0.5)
    print(exemplo_dado_quantitativo)
    time.sleep(0.5)
    print(f'DADOS QUANTITATIVOS:{dados_qualitativos}')
    time.sleep(0.5)
    print(exemplo_dado_qualitativo)

def questao2():
    comando = 'Nos casos a seguir, determine se faria um censo ou usaria amostragem e explique o motivo.'
    a = 'a) A idade média dos 115 residentes de uma comunidade de aposentados.'
    resposta_a = 'Senso'
    b = 'b) O tipo de filme mais popular entre os 100.000 assinantes de aluguel de filmes on-line.'
    resposta_b = 'Amostragem '
    print(f'\n{comando.upper()}\n')
    time.sleep(1.0)
    print(f'{a}: \nResposta: {resposta_b.upper()}\n')
    time.sleep(1.0)
    print(f'{b}: \nResposta: {resposta_a.upper()}\n')

def questao3():
    comando = str('Cinco notas de testes são apresentadas a seguir. As quatro primeiras notas equivalem a 15% da nota final e a última é 40% da nota final. \nEncontre a média ponderada das notas.')
    notas = [85, 92, 84, 89, 91]
    media_ponderada = float( (((notas[0] + notas[1] + notas[2] + notas[3])*15) + (notas[4]*40))/ (15 + 40) )
    print(f'{comando.upper()}\n')
    time.sleep(1.0)
    print(f'Média: {media_ponderada}')

def questao4():
    comando = str('Em um estudo sobre os hábitos de consumo online, 2.500 usuários de uma plataforma foram entrevistados. \nQueremos determinar a porcentagem desses usuários que preferem compras online em relação às compras em lojas físicas. \nQual seria o tamanho mínimo da amostra aleatória simples necessário para garantir um erro amostral máximo de 2,5%?')
    tamanho_da_amostra = 2500 
    erro = 2.5/100
    primeira_aproximacao = 1/(erro**2)
    tamanho = (primeira_aproximacao*tamanho_da_amostra)/(primeira_aproximacao+tamanho_da_amostra)
    print(f'{comando.upper()}\n')
    time.sleep(1.0)
    print(f'Tamanho: {tamanho}')

def questao5():
    comando = 'Considere a seguinte amostra aleatória das idades - em anos completos - dos alunos de um determinado curso.\nCom relação a essa amostra, calcule a média, moda e mediana; e construa a tabela frequência.'
    lista = [29, 27, 25, 39, 29, 27, 41, 31, 25, 33, 27, 25, 25, 
             23, 27, 27, 32, 26, 24, 36, 32, 26, 28, 24, 28, 27, 
             24, 26, 30, 26, 35, 26, 28, 34, 29, 23, 28]
    lista.sort()
    lista = np.array(lista)
    mediana = np.median(lista)
    soma = np.sum(lista)
    media = soma/len(lista)
    print(comando.upper())
    time.sleep(1.0)
    print(f'Mediana: {mediana}')
    time.sleep(1.0)
    print(f'Média: {media}')
    time.sleep(1.0)
    moda(lista)
    tabela_de_frequencia(lista)

def questao7():
    comando = [['Os dados a seguir representam as idades (em anos) de pessoas que participaram de um campeonato de tênis de mesa:'], ['a) Tabela frequência:'], ['b) Média, moda e mediana'],['c) Q1 e Q3'], ['d) P40']]
    lista = [25, 32, 20, 28, 22, 36, 19, 31, 24, 27, 35, 29, 26, 21, 23, 37, 30, 18, 34, 39, 38, 33, 40, 25,
             19, 28, 22, 31, 36, 20, 27, 33, 35, 24, 26, 30, 38, 29, 32, 23, 37, 21, 34, 18, 39, 40, 19, 22,
             25, 28]
    for frases in comando:
        for sequencia in frases:
            if sequencia == comando[0][0]:
                print(f'\n{sequencia.upper()}\n')
                time.sleep(1.0)
            else:
                print(f'{sequencia.upper()}')
                time.sleep(1.0)
    tabela_de_frequencia(lista)
    moda(lista)
    time.sleep(0.5)
    media_aritmetica(lista)
    time.sleep(0.5)
    mediana(lista)
    quartil(1, lista)
    time.sleep(0.5)
    quartil(3, lista)
    time.sleep(0.5)
    percentil(40, lista)

