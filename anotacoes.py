class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data): # Função para colocar os elementos dentro da pilha 
        # ______________Complete aqui______________

    def pop(self):
        # ______________Complete aqui______________


    def get(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next_node
        return elements


def main():
    stack = Stack()

    elements = input() # O input vai ser colocado aqui

    for element in elements.split(): # Separar o input 
        stack.push(element) # Vai adicionar os elementos na pilha

    print(f"Pilha: {stack.get()}")

    for _ in range(len(elements.split())):
        popped_element = stack.pop()
        print(f"Removido: {popped_element}")
        print(f"Pilha: {stack.get()}")

if __name__ == "__main__":
    main()


# DUVIDAS: como colocar os dados no topo
# Lista encadeada

# Tipos abstratos de dados: é um "contrato" de como vai ser usado aquele dado

# Pesquisar dados vazios em python 
#terminar as anotações do numpy e depois checar o material do classroom para complementar 
link = 'https://www.youtube.com/watch?v=-KdGmnEcC4k' 
musica de rock das antigas


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.pai = None
        self.direita = None
        self.esquerda = None

class MaxHeap:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        item = Node(int(valor))  # Convert valor to an integer

        if self.raiz is None:
            self.raiz = item
        else:
            self._inserir_recursivo(self.raiz, item)

    def _inserir_recursivo(self, node, novo_item):
        if node.esquerda is None:
            node.esquerda = novo_item
            novo_item.pai = node
            self._sobe_heap(novo_item)
        elif node.direita is None:
            node.direita = novo_item
            novo_item.pai = node
            self._sobe_heap(novo_item)
        else:
            # Escolhe o lado com menos elementos para manter a propriedade de árvore completa
            if self._altura(node.esquerda) <= self._altura(node.direita):
                self._inserir_recursivo(node.esquerda, novo_item)
            else:
                self._inserir_recursivo(node.direita, novo_item)

    def _sobe_heap(self, node):
        while node.pai is not None and node.pai.valor < node.valor:
            node.pai.valor, node.valor = node.valor, node.pai.valor
            node = node.pai

    def _altura(self, node):
        if node is None:
            return 0
        return 1 + max(self._altura(node.esquerda), self._altura(node.direita))

    def percorre(self, node, lista):
        if node:
            self.percorre(node.esquerda, lista)
            lista.append(node.valor)
            self.percorre(node.direita, lista)

# Exemplo de uso:
heap = MaxHeap()
lista = input().split(',')
listaaa = []
for i in lista:
    heap.inserir(i)

heap.percorre(heap.raiz, listaaa)
for i in listaaa:
    if i != listaaa[-1]:
        print(i, end= ' ')
    else:
        print(i)
primeiro_elemento = heap.raiz.valor
segundo_valor = 0
if heap.raiz.direita.valor > heap.raiz.esquerda.valor:
    segundo_valor = heap.raiz.direita.valor
elif heap.raiz.direita.valor < heap.raiz.esquerda.valor:
    segundo_valor = heap.raiz.esquerda.valor
else:
    segundo_valor = heap.raiz.direita.valor
print(f'R${primeiro_elemento*segundo_valor}')


# QUESTÃO TABELA HASH DIKASTIS

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
