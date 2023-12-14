# ------------------------ TABELA HASH --------------------------

"""Será fornecido um valor 'Qualquer coisa', daí será processado por uma função que irá fazer um cálculo e descobrirá o indice que esse 'Qualquer coisa' ficará numa lista"""

# Exemplo: tenho a lista = [1055, 1492, 1776, 1918 e 1945, 1812] e quero descobrir em qual indice o elemento vai ficar na tabela hash. 
# O espaço de chaves são os números inteiros de quatro dígitos

# Deseja-se traduzi-los no conjunto [0,1,2,3,4,5,6,7], ou seja, 8 espaços.
# Irá ser utilizado o mod 8, porque o máximo resto é 7 e o mínimo é um número divisível por 8, resto 0.

# Uma possível função hash seria f(x) = (5 • x) mod 8, que gerará o seguinte saída:

""" f (1055) = (5 • 1055) mod 8 = 5275 mod 8 = 3
    f (1492) = (5 • 1492) mod 8 = 7460 mod 8 = 4
    f (1776) = (5 • 1776) mod 8 = 8880 mod 8 = 0
    f (1918) = (5 • 1918) mod 8 = 9590 mod 8 = 6
    f (1945) = (5 • 1945) mod 8 = 9725 mod 8 = 5
    f (1812) = (5 • 1812) mod 8 = 9060 mod 8 = 4 """













# Questão dikastis 1

class Node:
    def __init__(self, dado):
        self.dado = dado
        self.indice_do_dado_na_lista = None

def separar_grupos(string):
    string = str(string)
    grupos = []
    lista_aux = []
    for i in string:
        if i not in lista_aux:
            lista_aux.append(i) 
        else: 
            grupos.append(Node(lista_aux))
            lista_aux = []
            lista_aux.append(i)
    if lista_aux not in grupos and lista_aux != []:
        grupos.append(Node(lista_aux))
    return grupos

def calculo_posicao_do_grupo_por_tabela_ascii(grupos): # Essa função vai fazer o calculo do numero na tabela e vai calcular o resto
    # TRECHO O(n²)
    for no in grupos:
        grupo = no.dado
        numero_ascii_grupo = 0
        for letra in grupo:
            numero_ascii_grupo += ord(letra)
        no.indice_do_dado_na_lista = numero_ascii_grupo % 10

def alocação_grupo(grupo, agenda_shifu): # Vai corrigir as colisões
    posicao_na_lista = grupo.indice_do_dado_na_lista

    while agenda_shifu[posicao_na_lista] != 'vago':
        posicao_na_lista = (posicao_na_lista + 1) % 10

    agenda_shifu[posicao_na_lista] = grupo.dado

#separar grupos
string = str(input())
grupos = separar_grupos(string)

#cria a agenda
agenda_shifu = [ 'vago' for i in range(10) ] 

# Vai calcular os numeros e suposta posição dos grupos
calculo_posicao_do_grupo_por_tabela_ascii(grupos) 

# colocação dos grupos nos lugares devidos
for grupo in grupos:
    alocação_grupo(grupo, agenda_shifu) 
print(agenda_shifu) #finish











