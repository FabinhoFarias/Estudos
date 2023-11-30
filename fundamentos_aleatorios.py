import random

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

def combinação_de_ordenadas():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lista = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n] #nos ranges entra x+1 por conta da exclusão do ultimo n
    print(lista)
#combinação_de_ordenadas()

def reverseee(lista):
    #print(lista) # printa a lista no começo
    outra_lista = []
    if not lista:
        print([])
    else:
        for i in lista:
            outra_lista.insert(0, i)
        #print(outra_lista) # printa a lista invertida
        return outra_lista
    #OUTRO JEITO DE FAZER
    """def inverte(nums):
        #Inverte o conteúdo da lista de entrada.
        inicio = 0
        fim = len(nums) - 1
        while inicio < fim:
            # Note a forma elegante de trocarmos o conteúdo das variáveis.
            nums[inicio], nums[fim] = nums[fim], nums[inicio]
            inicio += 1
            fim -= 1
        return nums"""
list = [1,2,3,4,5,6,7,8,9,10]
list.reverse()

def confere_inversao(n, m):
    """Checa o resultado da função `inverte` em n listas de tamanho m geradas aleatoriamente."""
    for i in range(n):
        # Cria uma lista com números aleatórios no intervalo [0, m].
        nums1 = [random.randint(0, m) for a in range(m)]

        # Cria uma lista com os mesmos elementos de nums1.
        nums2 = nums1[:]

        # Inverte a lista nums1 usando a biblioteca padrão de Python.
        nums1.reverse()

        # Invoca nosso algoritmo para inverter nums2 e confere o resultado.
        if reverseee(nums2) == nums1:
            print("Sucesso!")
