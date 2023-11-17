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
