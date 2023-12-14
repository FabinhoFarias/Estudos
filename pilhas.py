#--------------------------------------------PILHAS-------------------------------------------------------------------------------------------------------

class Node:
    def __init__(self, data): # Precisa ser inserido apenas o primeiro dado
        self.data = data
        self.next = None      # "next" é a informação para o próximo dado, iniciado com vazio


"""Conceito de Pilhas: Uma pilha é uma estrutura de dados linear que segue a ordem Last In, First Out (LIFO), 
                       o que significa que o último elemento inserido é o primeiro a ser removido. 
                       Isso é análogo a uma pilha de pratos, onde você adiciona um prato no topo e remove sempre o prato mais recente que foi adicionado."""

# Elementos Principais: Topo da Pilha: O ponto de acesso para inserção (push) e remoção (pop) de elementos. É o local onde as operações são realizadas.
#                       Base da Pilha: O ponto oposto ao topo, onde a pilha começa. É o local onde os elementos permanecem constantes.

"""Operações Básicas em Pilhas: Push:        Adicionar um elemento no topo da pilha.
                                Pop:         Remover o elemento do topo da pilha.
                                Peek ou Top: Visualizar o elemento no topo da pilha sem removê-lo."""

class Nodo_pilha: # Nova classe de nó para usar na pilha, pois vai ter um topo e um anterior
    """Esta classe representa um nodo de uma estrutura encadeada."""
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior
        
class Pilha:
    """Esta classe representa uma pilha usando uma estrutura encadeada."""
    def __init__(self):
        self.topo = None
    def insere(self, novo_dado):
        """Insere um elemento no final da pilha."""
        novo_nodo = Nodo_pilha(novo_dado) # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo.anterior = self.topo    # Faz com que o novo nodo seja o topo da pilha.
        self.topo = novo_nodo             # Faz com que a cabeça da lista referencie o novo nodo.

    def remove(self):
        """Remove o elemento que está no topo da pilha."""
        assert self.topo, "Impossível remover valor de pilha vazia."
        self.topo = self.topo.anterior
