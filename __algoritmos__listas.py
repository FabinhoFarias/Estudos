#--------------------------------------------LISTAS EM ALOCAÇÃO SEQUENCIAL----------------------------------------------------------------------------------------

# É possível encontrar um elemento de forma aleatória no python através do seu índice. Por exemplo, i[n] irá retornar o [n-ésimo - 1] termo da lista de forma automática. Isso é O(1). 
""" 1 - Dinamicamente Tipada:         Python permite criar listas sem declarar explicitamente os tipos dos elementos, facilitando a inclusão de diferentes tipos.
    2 - Alocação Dinâmica de Memória: A quantidade de memória necessária para armazenar elementos em uma lista é alocada dinamicamente, permitindo o crescimento ou a redução da lista conforme necessário.
    3 - Objetos Referenciados:        Os elementos de uma lista são referências a objetos, não os próprios objetos, proporcionando flexibilidade para lidar com tipos diferentes.
    4 - Tamanho Dinâmico:             O tamanho de uma lista pode ser alterado durante a execução do programa, permitindo adição ou remoção de elementos de forma flexível."""

# ATENÇÃO: Listas em Python são listas encadeadas, e como tal, elas podem armazenar elementos de tipos diferentes, que não necessariamente estão em posições contíguas de memória, e não possuem tamanho fixo.

# Tópico 3 é um ponteiro. Em Python, as listas guardam um endereço (ponteiro) de onde está o objeto.
def exemplo_de_referencia_do_ponteiro():
    """Exemplo"""
    lista = [1, 2, 3]
    print(lista)
    outra_lista = lista
    print(outra_lista)
    lista = lista.append([4]) # Mesmo alterando só a primeira lista, como a segunda aponta para o mesmo lugar da primeira, a mudança terá efeito na segunda tambem. [1, 2, 3, [4]]
    print(outra_lista) 

# ALGORITIMOS DE BUSCA EM UMA LISTA :

"""Alocação sequencial"""


# Se para achar um elemento numa lista com seu indice é O(1), para achar o indice de um elemento numa lista a complexidade muda. 
# Busca linear em lista em alocação sequencial
def alocação_sequencial_busca_indice(lista, elem):
    """Retorna o índice elem se ele estiver na lista ou None, caso contrário"""
    for i in range(len(lista)): # Percorre a lista inteira (n)
        if lista[i] == elem:    # Percorre a lista inteira (n)
            return i  # +1 operação
    return None       # +1 operação
    # complexidade: n + n + 1 = 2n + 1, O(n)
def exemplo_de_busca_num_lista():
    lista_estranha = [8, "5", 32, 0, "python", 11]
    print(f'Itens na lista: {lista_estranha}')
    elemento = input('digite um elemento: Ex: "python" ')
    indice = alocação_sequencial_busca_indice(lista_estranha, elemento)
    if indice is not None:
        print("O índice do elemento {} é {}".format(elemento, indice))
    else:
        print("O elemento {} não se encontra na lista".format(elemento))

# INSERÇÃO E REMOÇÃO:

# Inserção: O pior caso, é quando precisa ser inserido um elemento na primeira posição. Todos os elementos serão arrastados uma casa para a direita e o algoritimo precisará percorrer n-1 casas da lista.
#           O melhor caso é para inserir na ultima posição, pois só precisará criar um espaço de memória.

def alocação_sequencial_insercao_ultima_posicao(lista, elemento):
    lista.append(elemento)
    print(lista)
    return lista

def alocação_sequencial_insercao_primeira_posicao(lista):
    elemento = input()
    index = 0
    lista.append('Qualquer coisa') # Insere-se qualquer coisa na ultima posição
    lista[1 : len(lista)] = lista[:-1] # DUVIDA: Esse passo ainda vai ser dependente de N ?
    lista[0] = elemento
    return lista
# Remoção:  O pior caso, é quando precisa ser removido um elemento na ultima posição. O algoritimo precisará percorrer n-1 casas da lista.
#           O melhor caso é para remover na primeira posição, pois só precisará remover um espaço de memória no inicio da lista.

def alocação_sequencial_remoção_ultima_posicao(lista):
    lista.pop()
    return lista

def alocação_sequencial_remoção_primeira_posicao(lista):
    lista.pop(0)
    return lista

#--------------------------------------------LISTAS EM ALOCAÇÃO ENCADEADA----------------------------------------------------------------------------------------

# Na sequencial, precisa-se reservar um espaço pré definido de memória e a partir da inserção ou remorção poder ser feito o reajuste da memória.
# A alocação dinâmica, permite que os dados sejam armazenados em locais quaisquer da memória e esses espaços serão alocados nomento que for preciso armazenar um novo elemento.

# Uma lista encadeada é uma sequência de nós, um ligado ao outro, de forma que um nó sabe quem é o próximo nó.
# Basta saber o primeiro nó e todos os outros serão sabidos.

# Em uma lista encadeada, um nó é uma estrutura que contém um valor e uma referência (ou ponteiro) para o próximo nó na sequência. Cada nó é independente e possui uma referência ao próximo nó na lista.
"""EXEMPLO DE NÓ"""
class Node:
    def __init__(self, data): # Precisa ser inserido apenas o primeiro dado
        self.data = data
        self.next = None      # "next" é a informação para o próximo dado, iniciado com vazio

"""CONSTRUÇÃO DE UMA LISTA ENCADEADA"""

# Embora uma lista encadeada tenha uma construção diferente, ela ainda é uma lista. Ou seja, é necessário que haja métodos que listas normais tenham. As diferenças entre ambas é a complexidade, mas a interface precisa ser a mesma.
# append, pop, remove, printar um elemento de uma posição específica dado um index são exemplos do que precisa ser feito. 

class Lista_Encadeada:
    def __init__(self):
        self._primeiro_elemento = None  # Essa lista sempre começa vazia ( lista = [] )
        self._len = 0                   # Como começa vazia, seu tamanho é 0
    
    def __len__(self):  # Essa assinatura __len__(self) com  2 _ significa que é uma função especial
        return self._len

    def append(self, elemento):       # Esse método vai se comportar como o append numa lista normal.
        if self._primeiro_elemento:  # Quando já há alguém na primeira posição   
            ponteiro = self._primeiro_elemento  # Esse ponteiro vai assumir o primeiro elemento da lista
            while ponteiro.next:  # O loop vai verificar se há alguém na próxima posição
                ponteiro = ponteiro.next  # Se houver, o ponteiro é atualizado para o próximo elemento e o loop vai ser processado até que haja um None
            ponteiro.next = Node(elemento)  # Quando o loop parar e for None, cria-se um novo nó com o elemento passado como parâmetro da função.
            self._len += 1  # Recebe mais um no tamanho, pois foi adicionado um novo elemento na lista
        else:  # Quando não há alguém na primeira posição
            self._primeiro_elemento = Node(elemento)  # Cria-se o primeiro nó e o elemento será inserido na lista
            self._len += 1

    def insert(self, elemento, index=None):
        if elemento is None:  # Caso o primeiro elemento não exista
            raise ValueError("Elemento não pode ser None")
        elif index is not None:  # Caso especifique o index
            if self._primeiro_elemento:
                if index > self._len - 1:  # Caso o index seja maior que o tamanho da lista, vai inserir na última posição
                    ponteiro = self._primeiro_elemento  # Esse ponteiro vai assumir o primeiro elemento da lista
                    while ponteiro.next:  # O loop vai verificar se há alguém na próxima posição
                        ponteiro = ponteiro.next  # Se houver, o ponteiro é atualizado para o próximo elemento e o loop vai ser processado até que haja um None
                    ponteiro.next = Node(elemento)  # Quando o loop parar e for None, cria-se um novo nó com o elemento passado como parâmetro da função.
                    self._len += 1  # Recebe mais um no tamanho, pois foi adicionado um novo elemento na lista
                else:
                    ponteiro = self._primeiro_elemento
                    for i in range(index - 1):  # Ajustado para começar do índice 0
                        ponteiro = ponteiro.next
                    novo_no = Node(elemento)
                    novo_no.next = ponteiro.next
                    ponteiro.next = novo_no
                    self._len += 1
            else:  # Caso esteja vazia, cria-se o primeiro nó
                self._primeiro_elemento = Node(elemento)  # Cria-se o primeiro nó e o elemento será inserido na lista
                self._len += 1
        else:  # Vai repetir a função append
            if self._primeiro_elemento:  # Quando já há alguém na primeira posição   
                ponteiro = self._primeiro_elemento  # Esse ponteiro vai assumir o primeiro elemento da lista
                while ponteiro.next:  # O loop vai verificar se há alguém na próxima posição
                    ponteiro = ponteiro.next  # Se houver, o ponteiro é atualizado para o próximo elemento e o loop vai ser processado até que haja um None
                ponteiro.next = Node(elemento)  # Quando o loop parar e for None, cria-se um novo nó com o elemento passado como parâmetro da função.
                self._len += 1  # Recebe mais um no tamanho, pois foi adicionado um novo elemento na lista
            else:  # Quando não há alguém na primeira posição
                self._primeiro_elemento = Node(elemento)  # Cria-se o primeiro nó e o elemento será inserido na lista
                self._len += 1

    def print_lista(self, index=None):
        if index is not None: # Se index não for vazio ele printa um elemento específico
            if (int(index) >= self._len) or (int(index) < 0):
                raise IndexError("Index out of range")
            ponteiro = self._primeiro_elemento
            for i in range(index):
                ponteiro = ponteiro.next
            print(ponteiro.data)
        else:                 # Se for None, vai printar a lista toda. O(n)
            lista = []
            ponteiro = self._primeiro_elemento
            while ponteiro:
                lista.append(ponteiro.data)
                ponteiro = ponteiro.next
            print(lista)
    def pop(self, elemento=None, index=None):
        if self._primeiro_elemento:
            if elemento is None and index is None:
                if self._len == 1:  # Se há apenas um elemento na lista
                    popped_data = self._primeiro_elemento.data
                    self._primeiro_elemento = None
                    self._len -= 1
                    return popped_data
                else:
                    ponteiro = self._primeiro_elemento
                    for i in range(self._len - 2):  # Alterado para -2
                        ponteiro = ponteiro.next
                    popped_data = ponteiro.next.data
                    ponteiro.next = None
                    self._len -= 1
                    return popped_data
            elif index is not None:
                if index >= self._len or index < 0:
                    raise IndexError("Index out of range")
                if index == 0:  # Remover o primeiro elemento
                    popped_data = self._primeiro_elemento.data
                    self._primeiro_elemento = self._primeiro_elemento.next
                    self._len -= 1
                    return popped_data
                else:
                    ponteiro = self._primeiro_elemento
                    for i in range(index - 1):
                        ponteiro = ponteiro.next
                    popped_data = ponteiro.next.data
                    ponteiro.next = ponteiro.next.next
                    self._len -= 1
                    return popped_data
        else:
            raise IndexError("Pop from an empty list")
