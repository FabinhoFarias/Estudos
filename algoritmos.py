import numpy as np
#As anotações são baseadas na disciplina de algoritimos do CIn-UFPE do curso de SI

#DEFINIÇÃO: um algoritmo é uma sequência de passos computacionais que transformam a ENTRADA na SAÍDA. 
#Também podemos visualizar um aigoritmo como uma ferramenta para resolver umproblema computacional bem especificado

# Objetivo da aula: Apresentar os conceitos de Vetores, Matrizes e Tensores, ilustrando-os em Python utilizando a biblioteca numpy.
"""
Em Python, listas são estruturas nativas que permitem o armazenamento sequencial de diversos valores. Mas em alguns contextos elas são ineficientes. 
Vetores, matrizes e tensores são alternativas a listas para armazenamento de múltiplos valores de mesmo tipo (estruturas homogêneas)
Os dados são armazenados de forma contígua na memória (endereços sequenciais para blocos de mesmo tamanho), permitem indexar os elementos de forma direta (o que é mais eficiente de que em listas)
"""

# ----------------------------------------------------VETORES ---------------------------------------------------------------------------------------------

# Vetores são estruturas UNIDIMENSIONAIS que armazenam elementos de um mesmo tipo.
# Numpy oferece suporte a vetores em Python encapsulando-os em objetos da classe "ndarray" (signidica numero dimensão array, ou. um array multidimensional)
# Como os dados são armazenados contiguamente, é preciso informar o tipo dos dados a ser guardado e sua quantidade.
"""Olhar o 'numpy_resumo.py' para construir vetores com o numpy"""
#-------------------------------------ATIVIDADES DO PDF----------------------------------------------------------------------------------------------------

# QUESTÕES PARA VETORES

"""Q1 - Construa um programa que preenche um vetor de inteiros de 100 números, colocando 0 nas posições pares e 1 nas ímpares."""
def questao_1_vetores():
    contador = 0
    vetor = np.ones((1, 100))
    for posicao in vetor[0]:
        if contador % 2 == 0:
            vetor[0][contador] = 0
        contador +=1
    print(vetor)

"""Q2 - Construa um programa que lê, soma e imprime o resultado da soma de um vetor de inteiros de 10 posições."""
def questao_2_vetores():
    vetor = np.linspace(1, 100, num=10, endpoint=True) # Lembrar que o primeiro parâmetro e inclusivo e o segundo é exclusivo!
    soma = np.sum(vetor)
    print(f'Soma: {soma}')

"""Q3 - Construa um programa que multiplique os valores de um vetor de reais de 20 posições pelos valores de um outro vetor de reais de 20 posições. O
primeiro vetor deve ser inicializado com valores crescentes a partir de 1 e o segundo vetor com valores decrescentes a partir de 20. Os resultados das
multiplicações devem ser armazenados num terceiro vetor."""
def questao_3_vetores():
    vetor_crescente = np.linspace(1, 20, num=20, endpoint=True) # Cria um vetor crescente
    vetor_decrescente = np.sort(vetor_crescente, kind='heapsort')# A partir do crescente, cria-se o decrescente
    produto_escalar = np.dot(vetor_crescente, vetor_decrescente)# Faz o PRODUTO ESCALAR dos dois vetores
    print(produto_escalar)

"""Q4 - Leia um vetor de 16 posições e troque os 8 primeiros valores pelos 8 últimos e vice-versa. Escreva ao final o vetor obtido."""
def questao_4_vetores():
    vetor = np.linspace(1, 16, num=16, endpoint=True) # Lembrar que o primeiro parâmetro e inclusivo e o segundo é exclusivo!
    print(vetor)
    primeira_metade = vetor[0: int((len(vetor)/2))]#Quebra o vetor na metade
    segunda_metade = vetor[int((len(vetor)/2)): ]#Quebra o vetor na metade
    print(primeira_metade)
    print(segunda_metade)
    #print((len(vetor)/2))
    vetor = np.array([])
    resultado = np.concatenate((segunda_metade, primeira_metade), axis=0)
    print(resultado)

# QUESTÕES PARA MATRIZES

"""Q1 - Construa um algoritmo que efetue e apresente o resultado da soma entre duas matrizes 3 x 5. Inicialize a matriz com valores quaisquer e imprima o resultado na tela."""
def questao_1_matrizes():
    contador = 0
    # CONDIÇÃO: As matrizes devem ser n x k
    # Dada as matrizes A + B = C, A[linha][coluna] + B[linha][coluna] = C[linha][coluna]
    matriz_1 = np.zeros((3 ,5), dtype=float)
    dimensoes = matriz_1.shape
    print(f'Matriz 1: \n{matriz_1}')
    matriz_2 = np.ones((3 ,5), dtype=int)
    matriz_reposta = np.empty((dimensoes[0], dimensoes[1]), dtype=float)
    array_para_append = np.array([])
    print(f'Matriz 2: \n{matriz_2}\n')
    #RESOLUÇÃO: faz a soma escalar das linhas da matriz
    for linha_matriz_1, linha_matriz_2 in zip(matriz_1, matriz_2): # laço com as 2 matrizes
        for elemento_linha_matriz_1, elemento_linha_matriz_2 in zip(linha_matriz_1, linha_matriz_2):
            soma_elementos = elemento_linha_matriz_1 + elemento_linha_matriz_2
            array_para_append = np.append(array_para_append, soma_elementos)
            print(f'{elemento_linha_matriz_1} + {elemento_linha_matriz_2} = {soma_elementos}')
        matriz_reposta[contador] = array_para_append
        array_para_append = np.array([])
        contador += 1
    print(matriz_reposta)

"""Q2 - Faça um programa que multiplica uma matriz 3 x 3 de inteiros por um escalar k e imprima o resultado na tela. O usuário deve fornecer os valores da matriz e de k."""
def questao_2_matrizes():
    matriz = np.ones((3 ,3), dtype=int)
    numero_de_linhas = 0
    numero_de_colunas = 0
    for linha in matriz:
        numero_de_linhas += 1
        for elemento in linha:
            numero_de_colunas += 1
            elemento = int(input(f'A{numero_de_lihas}{numero_de_colunas}: '))
            matriz[(numero_de_linhas-1)][(numero_de_colunas-1)] = elemento
        numero_de_colunas = 0
    K = int(input('Constante: '))
    #dimensoes = matriz_1.shape
    print(f'Matriz: \n{matriz}')
    #matriz_reposta = np.empty((dimensoes[0], dimensoes[1]), dtype=float)
    #RESOLUÇÃO: faz a soma escalar das linhas da matriz
    numero_de_linhas = 0
    numero_de_colunas = 0
    for linha in matriz:
        numero_de_lihas += 1
        for elemento in linha:
            numero_de_colunas += 1
            elemento *= K
            novo_elemento = elemento
            print(f'A{numero_de_lihas}{numero_de_colunas} x {K} = {novo_elemento} ')
            matriz[(numero_de_linhas-1)][(numero_de_colunas-1)] = novo_elemento
        numero_de_colunas = 0
    print(matriz)
 
"""Q3 - Leia uma matriz 20 x 20. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final escrever a localização (linha e coluna) ou uma mensagem de “não 
encontrado."""
def questão_3_matrizes():
    numero_de_linhas = 0
    numero_de_colunas = 0
    matriz = np.random.randint(1, 401, size=(20,20))
    elemento_busca = float(input(f'Float: '))
    matriz_ordenada = np.sort(matriz)
    print(f'{matriz}\n\n{matriz_ordenada}')
    indices = np.where(matriz_ordenada == elemento_busca)
    print(indices)

"""Q4 - Dada uma matriz 5x5, elabore um algoritmo que imprima:"""
"""Parte 1: A diagonal principal"""
def questão_4_matrizes_parte_1():
    matriz = np.random.randint(1, 401, size=(5,5))
    numero_de_linhas = 0
    numero_de_colunas = 0
    for linha in matriz:
        for elemento in linha:
            if numero_de_colunas == numero_de_linhas:
                print(f'Elementos da diagonal principal: {matriz[numero_de_linhas][numero_de_colunas]}')
            numero_de_colunas += 1
        numero_de_colunas = 0
        numero_de_linhas += 1
"""Parte 2: A diagonal secundária"""
def questão_4_matrizes_parte_2():
    matriz = np.random.randint(1, 401, size=(5,5))
    print(matriz)
    numero_de_linhas = 0
    numero_de_colunas = 5
    for linha in matriz:
        numero_de_colunas -= 1
        print(f'Elementos da diagonal secundária: {matriz[numero_de_linhas][numero_de_colunas]}')
        numero_de_linhas += 1
"""Parte 3: A soma da linha 4"""
def questão_4_matrizes_parte_3():
    numero_de_linhas = 0
    numero_de_colunas = 0
    matriz = np.random.randint(1, 401, size=(5,5))
    soma_linha_4 = 0
    for elemento in matriz[3]:
        soma_linha_4 += elemento
    print(f'Linha 4: {matriz[3]}')
    print(f'Soma da linha 4: {soma_linha_4}')
"""Parte 4: A soma da coluna 2"""
def questão_4_matrizes_parte_4():
    numero_de_linhas = 0
    numero_de_colunas = 0
    matriz = np.random.randint(1, 401, size=(5,5))
    soma_linha_1 = 0
    for elemento in matriz[1]:
        soma_linha_4 += elemento
    print(f'Linha 4: {matriz[1]}')
    print(f'Soma da linha 4: {soma_linha_1}')
"""Parte 5: Tudo, exceto a diagonal principal"""
def questão_4_matrizes_parte_5():
    matriz = np.ones((5, 5), dtype=int)
    numero_de_linhas = 0
    numero_de_colunas = 0
    for linha in matriz:
        for elemento in linha:
            if numero_de_colunas != numero_de_linhas:
                print(f'Elementos diferente da diagonal principal: {matriz[numero_de_linhas][numero_de_colunas]}')
            numero_de_colunas += 1
        numero_de_colunas = 0
        numero_de_linhas += 1

#--------------------------------------------ANÁLISE DE ALGORITIMOS---------------------------------------------------------------------------------------------

# COMPLEXIDDADE: Medida da quantidade de recursos que é demandada do computador para realizar determinado algoritimo. Ela independe da linguagem de programação e da 
#                máquina que vai rodar o algoritimo.

# Quando é falado sobre a complexidade de um algoritimo, esta sendo referenciado o pior caso e em como ela cresce em função da entrada N. 
# A notaçãio O() é usada para fazer menção ao comportamento da função que vai ser o termo de maior grau.
# Por exemplo,  a questão_4_matrizes_parte_5() tem 2 for, ou seja, ela vai percorrer n^2 vezes. Então, é um algoritimo O(n^2)

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





#--------------------------------------------PILHAS-------------------------------------------------------------------------------------------------------


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

#--------------------------------------------ÁRVORES-------------------------------------------------------------------------------------------------------


class Node_tree:
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
