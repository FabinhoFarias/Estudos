
#--------------------------------------------ÁRVORES-------------------------------------------------------------------------------------------------------

""" Árvores são estruturas de dados hierárquicas. Basicamente, árvores são formadas por um conjunto de elementos, os quais chamamos nodos (ou vértices) 
    conectados de forma específica por um conjunto de arestas. Um dos nodos, que dizemos estar no nível 0, é a raiz da árvore, e está no topo da hierarquia. 
    A raiz está conectada a outros nodos, que estão no nível 1, que por sua vez estão conectados a outros nodos, no nível 2, e assim por diante."""


# IMPLANTAR ÁRVORE BINÁRIA DE BUSCA----------------------------------

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.pai = None
        self.direita = None
        self.esquerda = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        item = Node(valor)

        if self.raiz == None:
            self.raiz = item
        
        else:
            adicionado = False
            itemAtual = self.raiz
            while not adicionado:
                if itemAtual.valor < item.valor:
                    if itemAtual.direita == None:
                        itemAtual.direita = item
                        item.pai = itemAtual
                        adicionado = True
                    else:
                        itemAtual = itemAtual.direita
                else:
                    if itemAtual.esquerda == None:
                        itemAtual.esquerda = item
                        item.pai = itemAtual
                        adicionado = True
                    else:
                        itemAtual = itemAtual.esquerda
"""Inserção de Nós:

Adiciona um novo nó à árvore.
Remoção de Nós:

Remove um nó específico da árvore.
Busca de Nós:

Procura por um valor específico na árvore.
Traversals (Percurso):


Calcula a altura da árvore.
Número de Nós:

Conta o número total de nós na árvore.
Mínimo e Máximo:

Encontra o valor mínimo e máximo na árvore.
Verificação se está Vazia:

Verifica se a árvore está vazia."""

class BSTNode(object):

    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def get(self, key):
        """Retorna uma referência ao nó de chave key
        """
        if self.key == key:
            return self
        node = self.left if key < self.key else self.right
        if node is not None:
            return node.get(key)

    def add(self, key):
        """Adiciona elemento à subárvore
        """
        side = 'left' if key < self.key else 'right'
        node = getattr(self, side)
        if node is None:
            setattr(self, side, BSTNode(key))
        else:
            node.add(key)
    
    def remove(self, key):
        """Remove da árvore o elemento de chave key
        """
        if key < self.key:
            self.left = self.left.remove(key)
        elif key > self.key:
            self.right = self.right.remove(key)
        else:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            t = self.right._min()
            self.key, self.value = t.key, t.value
            self.right._deleteMin()
        return self
    
    def _min(self):
        """Retorna o menor elemento da subárvore
        """
        if self.left is None:
            return self
        else:
            return self.left._min()
    
    def _deleteMin(self):
        """Remove da subárvore o menor elemento
        """
        if self.left is None:  # encontrou o min, daí pode rearranjar
            return self.right
        self.left = self.left._deleteMin()
        return self

    def traverse(self, visit, order='pre'):
        """Percorre a árvore na ordem fornecida como parâmetro (pre, pos ou in) 
           visitando os nós com a função visit() recebida como parâmetro.
        """
        if order == 'pre':
            visit(self.key)
        if self.left is not None:
            self.left.traverse(visit, order)
        if order == 'in':
            visit(self.key)
        if self.right is not None:
            self.right.traverse(visit, order)
        if order == 'post':
            visit(self.key)

    def _print_node(self, key):
        print(key, end=' ')  # Use a instrução de impressão diretamente

    def print(self, order='pre'):
        self.traverse(self._print_node, order)

# Exemplo de uso:
raiz = BSTNode(10)
raiz.add(5)
raiz.add(15)
raiz.add(3)
raiz.add(7)
raiz.add(12)
raiz.add(20)

print("Travessia em ordem:")
raiz.print(order='in')


# EXERCÍCIOS 
""" O menor elemento de uma BST é o nodo mais à esquerda na árvore. """
def minimo(raiz):
    nodo = raiz
    while nodo.esquerda is not None:
        nodo = nodo.esquerda
    return nodo.chave
""" O maior elemento de uma BST é o nodo mais à esquerda na árvore. """
def maximo(raiz):
    nodo = raiz
    while nodo.direita is not None:
        nodo = nodo.direita
    return nodo.chave
