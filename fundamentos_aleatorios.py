# Contar numeros num array
def encontrar_elemento_unico(lista):
    contador = {}
    
    # Contar a ocorrência de cada elemento na lista
    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1

    # Encontrar o elemento único
    for chave, valor in contador.items():
        if valor == 1:
            return chave

# Exemplos de uso
exemplos = [
    [7],
    [0],
    [1, 1, 2],
    [0, 1, 0, 1, 0],
    [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]
]

for exemplo in exemplos:
    resultado = encontrar_elemento_unico(exemplo)
    print(f"A lista {exemplo} retorna o elemento único: {resultado}")


#
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
