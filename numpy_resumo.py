import numpy
# Numpy oferece suporte a mais tipos de dados que básicos Python (checar a tabela que o numpy suporta)
# Algumas das funções básicas do numpy 



"""1. **numpy.array()**:    Usada para criar um array NumPy. Você pode passar uma lista ou uma sequência de números para criar um array."""
def funcao_numpy_array ():
    array = numpy.array([1, 2, 3, 4, 5, 6]) # transforma a lista fornecida em um array
    print(array)
    print(type(array))
#funcao_numpy_array()

"""2. **numpy.arange()**:   Cria um array com valores igualmente espaçados dentro de um intervalo."""
def funcao_numpy_arange():# Cria um array com valores de 0 a 9 (exclusivo) com um passo de 2
    array = numpy.arange(0, 10, 2)
    print(array)
    print(type(array))
#funcao_numpy_array()

"""3. **numpy.zeros()**:    Cria um array n-dimensional preenchido com zeros."""
def funcao_numpy_zeros():  # Recebe o parâmetro Shape e Type do array
    array = numpy.zeros(5) # Cria um array unidimensional de 5 elementos preenchido com zeros
    print(array)
    print(type(array))
#funcao_numpy_zeros()

"""4. **numpy.ones()**:     Cria um array preenchido com uns."""
def funcao_numpy_ones():  # Recebe o parâmetro Shape e Type do array
    array = numpy.ones((5, 5)) # Cria um array 5 x 5 preenchido com uns
    print(array)
    print(type(array))
#funcao_numpy_ones()

"""5. **numpy.empty()**:    Cria um array vazio (com valores iniciais não inicializados). """
def funcao_numpy_empty():
    array = numpy.empty((2, 3), dtype=int)# Cria um array bidimensional de 2x3 inteiro
    print(array)
    print(type(array))
#funcao_numpy_empty()

"""6. **numpy.linspace()**: Cria um array com valores igualmente espaçados entre dois números."""
def funcao_numpy_linspace():
    array = numpy.linspace(0, 1, num=10, endpoint=True)# Cria um array de 10 valores igualmente espaçados entre 0 e 1, incluindo 1
    print(array)
    print(type(array))
#funcao_numpy_linspace()

"""7. **numpy.reshape()**:  Permite alterar a forma de um array."""
def funcao_numpy_reshape():
    # Cria um array unidimensional com valores de 0 a 5
    array = numpy.array([0, 1, 2, 3, 4, 5])
    # Remodela o array para uma matriz 2x3
    reshaped_arr = numpy.reshape(array, (2, 3))
    print(f"Array remodelado:\n{reshaped_arr}")
    print(type(reshaped_arr))
#funcao_numpy_reshape()
# A função "numpy.reshape()" tem algumas restrições que devem ser observadas:
# Tamanho total constante:  O número total de elementos no array original deve ser igual ao número total de elementos no array remodelado. Isso significa que o produto das dimensões do array original deve ser igual ao produto das dimensões do array remodelado.
# Compatibilidade de forma: A nova forma especificada deve ser compatível com a forma do array original. Por exemplo, você não pode tentar remodelar um array unidimensional em uma matriz 3x3, a menos que o array original tenha 9 elementos.
# Dados não são copiados:   A função não realiza cópias dos dados, apenas reorganiza a forma dos elementos no array original. Portanto, qualquer modificação nos elementos do array remodelado afetará o array original e vice-versa.

"""8. **numpy.sum()**:      Calcula a soma dos elementos de um array."""
def funcao_numpy_sum():
    # Cria um array unidimensional com alguns valoresin
    arr = numpy.array([1, 2, 3, 4, 5])
    # Calcula a soma de todos os elementos no array
    soma = numpy.sum(arr)
    print("Soma dos elementos no array:", soma)
#funcao_numpy_sum()
# A complexidade dessa função é O(n) (n=tamanho da entrada)  

"""9. **numpy.mean()**:     Calcula a média dos elementos de um array."""
def funcao_numpy_mean():
    # Cria um array unidimensional com alguns valores
    array = numpy.array([1, 2, 3, 4, 5])
    #OBSERVAÇÃO: A função também é flexivel para matrizes nxn
    # Calcula a média dos elementos no array
    media = numpy.mean(array)
    print("Média dos elementos no array:", media)
#funcao_numpy_mean()

"""10. **numpy.min()** e **numpy.max()**: Encontram o valor mínimo e máximo em um array, respectivamente."""
def funcao_numpy_min():
    # Cria um array unidimensional com alguns valores
    arr = numpy.array([3, 1, 5, 2, 4])
    # Encontra o valor mínimo no array
    minimo = numpy.min(arr)
    print("Valor mínimo no array:", minimo)
#funcao_numpy_min()
#   AMBAS FUNCIONAM PARA MATRIZES 
def funcao_numpy_max():
    # Cria um array unidimensional com alguns valores
    arr = numpy.array([3, 1, 5, 2, 4])
    # Encontra o valor máximo no array
    maximo = numpy.max(arr)
    print("Valor máximo no array:", maximo)
#funcao_numpy_max()

"""11. **numpy.std()**:     Calcula o desvio padrão dos elementos de um array."""
def funcao_numpy_std(): # TAMBÉM FUNCIONA PARA MATRIZES E VETORES
    # Cria um array unidimensional com alguns valores
    arr = numpy.array([1, 2, 3, 4, 5])
    # Calcula o desvio padrão dos elementos no array
    desvio_padrao = numpy.std(arr)
    print("Desvio padrão dos elementos no array:", desvio_padrao)
#funcao_numpy_std()

"""12. **numpy.var()**:     Calcula a variância dos elementos de um array."""
def funcao_numpy_var(): # TAMBÉM FUNCIONA PARA MATRIZES E VETORES
    # Cria um array unidimensional com alguns valores
    arr = numpy.array([1, 2, 3, 4, 5])
    # Calcula a variância dos elementos no array
    variancia = numpy.var(arr)
    print("Variância dos elementos no array:", variancia)
#funcao_numpy_var()

"""13. **numpy.dot()**:     Realiza o produto escalar entre dois arrays."""
def funcao_numpy_dot():
    # Cria dois vetores (arrays unidimensionais)
    vetor1 = numpy.array([1, 2, 3])
    vetor2 = numpy.array([4, 5, 6])
    # Realiza o produto escalar entre os dois vetores
    # Produto Escalar = (1 * 4) + (2 * 5) + (3 * 6) = 4 + 10 + 18 = 32
    produto_escalar = numpy.dot(vetor1, vetor2)
    print("Produto escalar dos vetores:", produto_escalar)
#funcao_numpy_dot()

"""14. **numpy.transpose()**: Transpõe um array, trocando linhas por colunas."""
def funcao_numpy_transpose():
    # Cria uma matriz 2x3 com alguns valores
    matriz = numpy.array([[1, 2, 3],
                          [4, 5, 6]])
    # Transpõe a matriz (troca as linhas por colunas)
    matriz_transposta = numpy.transpose(matriz)
    print("Matriz original:")
    print(matriz)
    print("Matriz transposta:")
    print(matriz_transposta)
#funcao_numpy_transpose()

"""15. **numpy.concatenate()**: Concatena arrays ao longo de um eixo especificado."""
def funcao_numpy_concatenate():
    # Crie duas matrizes 2x3
    matriz1 = numpy.array([[1, 2, 3],
                           [4, 5, 6]])
    matriz2 = numpy.array([[7, 8, 9],
                           [10, 11, 12]])
    # Concatene as matrizes ao longo do eixo 1 (colunas)
    resultado = numpy.concatenate((matriz1, matriz2), axis=1)
    # IMPORTANTE: consultar os valores de 'axis' diferentes para cada dimensão diferente de matriz
    print("Matriz 1:")
    print(matriz1)
    print("Matriz 2:")
    print(matriz2)
    print("Resultado da concatenação ao longo do eixo 1:")
    print(resultado)
#funcao_numpy_concatenate()

"""16. **numpy.split()**: Divide um array em subarrays ao longo de um eixo especificado."""
def funcao_numpy_split():
    # Crie uma matriz 2x4
    matriz = numpy.array([[1, 2, 3, 4],
                          [5, 6, 7, 8]])
    # Use a função split para dividir a matriz em duas submatrizes ao longo do eixo 1 (colunas)
    submatrizes = numpy.split(matriz, 2, axis=1)
    print("Matriz original:")
    print(matriz)
    print("Submatriz 1:")
    print(submatrizes[0])
    print("Submatriz 2:")
    print(submatrizes[1])
#funcao_numpy_split()

"""17. **numpy.sort()**: Classifica os elementos de um array."""
def funcao_numpy_sort():
    # Crie uma matriz 1x4 não ordenada
    matriz = numpy.array([3, 1, 4, 2])
    # Ordene a matriz em ordem crescente (padrão)
    matriz_ordenada = numpy.sort(matriz)
    print("Matriz original:")
    print(matriz)
    print("Matriz ordenada em ordem crescente:")
    print(matriz_ordenada)
    # Para ordenar em ordem decrescente, você pode usar o parâmetro 'kind'
    matriz_decrescente = numpy.sort(matriz, kind='heapsort')
    print("Matriz ordenada em ordem decrescente:")
    print(matriz_decrescente)
    # A função 'numpy.sort()' também pode ser usada com matrizes multidimensionais
    matriz_2d = numpy.array([[3, 1, 4], [2, 6, 5]])
    # Ordene a matriz bidimensional ao longo do eixo 1 (colunas) em ordem crescente
    matriz_ordenada_2d = numpy.sort(matriz_2d, axis=1)
    print("Matriz bidimensional original:")
    print(matriz_2d)
    print("Matriz bidimensional ordenada ao longo do eixo 1 em ordem crescente:")
    print(matriz_ordenada_2d)
#funcao_numpy_sort()

"""18. **numpy.argmax()** e **numpy.argmin()**: Encontram os índices dos valores máximo e mínimo em um array, respectivamente."""
def funcao_numpy_sort():
    # Crie uma matriz 1x4 não ordenada
    matriz = numpy.array([3, 1, 4, 2])
    # Ordene a matriz em ordem crescente (padrão)
    matriz_ordenada = numpy.sort(matriz)
    print("Matriz original:")
    print(matriz)
    print("Matriz ordenada em ordem crescente:")
    print(matriz_ordenada)
    # Para ordenar em ordem decrescente, você pode usar o parâmetro 'kind'
    matriz_decrescente = numpy.sort(matriz)[::-1]
    print("Matriz ordenada em ordem decrescente:")
    print(matriz_decrescente)
    # A função 'numpy.sort()' também pode ser usada com matrizes multidimensionais
    matriz_2d = numpy.array([[3, 1, 4], [2, 6, 5]])
    # Ordene a matriz bidimensional ao longo do eixo 1 (colunas) em ordem crescente
    matriz_ordenada_2d = numpy.sort(matriz_2d, axis=1)
    print("Matriz bidimensional original:")
    print(matriz_2d)
    print("Matriz bidimensional ordenada ao longo do eixo 1 em ordem crescente:")
    print(matriz_ordenada_2d)# ordena nas colunas
#funcao_numpy_sort()

"""19. **numpy.where()**: Retorna os índices onde uma condição é verdadeira em um array."""
def funcao_numpy_where():
    # Crie um array unidimensional
    array = numpy.array([1, 2, 3, 4, 5])
    # Encontre os índices onde os elementos são maiores que 3
    indices = numpy.where(array > 3)
    print("Array original:")
    print(array)
    print("Índices onde os elementos são maiores que 3:")
    print(indices)
#funcao_numpy_where()

"""20. **numpy.random**: Módulo para geração de números aleatórios."""
""" O módulo numpy.random fornece uma variedade de funções para geração de números aleatórios. É amplamente utilizado em simulações, análise de dados e muitas outras aplicações onde a aleatoriedade é necessária. Aqui estão algumas funções importantes disponíveis no módulo numpy.random:
        numpy.random.rand(): Gera números aleatórios em uma distribuição uniforme entre 0 e 1.
        numpy.random.randn(): Gera números aleatórios a partir de uma distribuição normal (gaussiana) com média 0 e desvio padrão 1.
        numpy.random.randint(): Gera números inteiros aleatórios dentro de um intervalo especificado.
        numpy.random.uniform(): Gera números aleatórios em uma distribuição uniforme dentro de um intervalo especificado.
        numpy.random.normal(): Gera números aleatórios a partir de uma distribuição normal com média e desvio padrão especificados.
        numpy.random.seed(): Define a semente do gerador de números aleatórios, permitindo a reprodução dos mesmos resultados em diferentes execuções.
        numpy.random.shuffle(): Embaralha os elementos de um array ao longo do primeiro eixo.
        numpy.random.choice(): Gera amostras aleatórias a partir de um array ou sequência.
        Essas funções são apenas um subconjunto das muitas disponíveis no módulo numpy.random. Elas podem ser usadas para criar dados de teste, simulações e outras tarefas que envolvem números aleatórios."""

"""21. **numpy.eye()**: Cria uma matriz identidade com a diagonal principal de uns."""
def funcao_numpy_eye():
    # Crie uma matriz identidade 3x3
    matriz_identidade = numpy.eye(3) # Esse '3' pode ser n. Quando for n será uma matriz n por n
    print("Matriz Identidade 3x3:")
    print(matriz_identidade)
#funcao_numpy_eye()

"""22. Atributo shape em NumPy: O atributo shape é usado para descobrir a quantidade de elementos em cada dimensão de um vetor ou matriz em NumPy. Ele retorna uma tupla que representa o tamanho de cada dimensão."""
def funcao_numpy_shape():
    # Exemplo com uma matriz 2x3
    matriz = numpy.array([[1, 2, 3], [4, 5, 6]])
    dimensoes = matriz.shape
    print("Matriz:")
    print(matriz)
    print("Dimensões da matriz:")
    print(dimensoes)
#funcao_numpy_shape()

"""23. Atributo shape com np.arange(): O atributo shape pode ser usado com a função np.arange() para descobrir a quantidade de elementos em um vetor NumPy."""
def funcao_numpy_shape_com_arange():
    # Exemplo com np.arange()
    vetor = numpy.arange(10)
    dimensoes_vetor = vetor.shape
    print("Vetor:")
    print(vetor)
    print("Dimensões do vetor:")
    print(dimensoes_vetor) # Significa que ele vai ter 10 elementos ao longo da ultima dimensão
#funcao_numpy_shape_com_arange()

"""24. Atributo shape com numpy.full(): O atributo shape pode ser usado com a função numpy.full() para determinar as dimensões de uma matriz NumPy preenchida com valores constantes."""
def funcao_numpy_shape_com_full():
    # Exemplo com np.full()
    matriz = numpy.full((3, 4), 7.0)
    dimensoes_matriz = matriz.shape
    print("Matriz:")
    print(matriz)
    print("Dimensões da matriz:")
    print(dimensoes_matriz)  # Significa que a matriz terá 3 linhas e 4 colunas.
#funcao_numpy_shape_com_full()

#vstack




"""Estas são apenas algumas das muitas funções disponíveis no NumPy. Elas são amplamente utilizadas em análise de dados, processamento de sinais, cálculos científicos e muitas outras áreas. O NumPy é uma biblioteca poderosa e amplamente utilizada para trabalhar com arrays multidimensionais em Python."""


#Matrizes são criadas em numpy de forma similar a vetores, porém devem ser informadas as quantidades de dados para cada dimensão
