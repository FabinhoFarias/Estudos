import time
import random as rd
import numba

stop = True

while stop:
    entrada = int(input("Digite n: "))
    
    def tamanho_do_array(n):
        # Tamanho de n da lista
        tempo_inicial = time.time()
        lista = [rd.randint(1, 100) for _ in range(n)]
        tempo_final = time.time()
        tempo_de_resposta = tempo_final - tempo_inicial
        print(f'Duração random: {tempo_de_resposta}')
        return lista

    def soma(lista):
        soma = 0
        for i in lista:
            soma += i
        return soma

    lista = tamanho_do_array(entrada)

    tempo_inicial = time.time()
    resultado_soma = soma(lista)
    tempo_final = time.time()
    tempo_de_resposta = tempo_final - tempo_inicial

    print()
    print(f'Soma: {resultado_soma}')
    print(f'Duração do for: {tempo_de_resposta}')

    resposta = input("Deseja continuar? (S/N) ").strip().lower()
    if resposta != "s":
        stop = False
