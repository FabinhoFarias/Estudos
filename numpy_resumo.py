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
    # Cria um array unidimensional com alguns valores
    arr = numpy.array([1, 2, 3, 4, 5])
    # Calcula a soma de todos os elementos no array
    soma = numpy.sum(arr)
    print("Soma dos elementos no array:", soma)
funcao_numpy_sum()
# A complexidade dessa função é O(n) (n=tamanho da entrada)


"""9. **numpy.mean()**:     Calcula a média dos elementos de um array."""





"""10. **numpy.min()** e **numpy.max()**: Encontram o valor mínimo e máximo em um array, respectivamente."""
"""11. **numpy.std()**:     Calcula o desvio padrão dos elementos de um array."""
"""12. **numpy.var()**:     Calcula a variância dos elementos de um array."""




"""
#def tópico1 ():
13. **numpy.dot()**:     Realiza o produto escalar entre dois arrays.
#def tópico1 ():
14. **numpy.transpose()**: Transpõe um array, trocando linhas por colunas.
#def tópico1 ():
15. **numpy.concatenate()**: Concatena arrays ao longo de um eixo especificado.
#def tópico1 ():
16. **numpy.split()**: Divide um array em subarrays ao longo de um eixo especificado.
#def tópico1 ():
17. **numpy.sort()**: Classifica os elementos de um array.
#def tópico1 ():
18. **numpy.argmax()** e **numpy.argmin()**: Encontram os índices dos valores máximo e mínimo em um array, respectivamente.
#def tópico1 ():
19. **numpy.where()**: Retorna os índices onde uma condição é verdadeira em um array.
#def tópico1 ():
20. **numpy.random**: Módulo para geração de números aleatórios.
#def tópico1 ():
Estas são apenas algumas das muitas funções disponíveis no NumPy. Elas são amplamente utilizadas em análise de dados, processamento de sinais, cálculos científicos e muitas outras áreas. O NumPy é uma biblioteca poderosa e amplamente utilizada para trabalhar com arrays multidimensionais em Python.
"""




#Matrizes são criadas em numpy de forma similar a vetores, porém devem ser informadas as quantidades de dados para cada dimensão
