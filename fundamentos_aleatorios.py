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
