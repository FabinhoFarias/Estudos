import matplotlib.pyplot as plt
import numpy as np

#Para fazer um gráfico simples, usamos a função "plot". Ela recebe um número arbitrário de argumentos. O mais comum é usá-la da seguinte forma: plt.plot(x, y, formato)

#Aqui, x é uma sequência de COORDENADAS HORIZONTAIS: pode ser uma tupla, uma lista ou um array unidimensional. Analogamente, y é uma sequência de COORDENADAS VERTICAIS. (As sequências devem ter o mesmo tamanho)

#O parâmetro 'FORMATO' é uma string especificando rapidamente o "ESTILO DE GRÁFICO" (por exemplo: incluindo os caracteres r, g ou b o gráfico fica com cor vermelha, verde ou azul; - indica uma linha sólida e -- uma linha tracejada; o, s e ^ fazem marcadores em cima de cada ponto com formato de bolinha, quadrado ou triângulo). 

#O parâmetro formato é OPCIONAL, e por padrão o gráfico é feito com uma linha sólida ligando os pontos especificados. É possível passar parâmetros adicionais; veja a documentação para uma discussão detalhada.


#Por exemplo, vamos graficar as funções:
# y = x
# y = x²
# y = x³

def primeiro_gráfico():
    #O primeiro passo é gerar os valores de x que serão usados; aqui, usamos a função "linspace" do numpy. Em seguida graficamos as funções com a função plot e executamos o comando plt.show() para mostrar o gráfico na tela:
    x = np.linspace(0, 2, 21) # 21 pontos no intervalo [0, 2]
    plt.plot(x, x)            # função y = x

    plt.plot(x, x**2)         # função y = x^2

    plt.plot(x, x**3)         # função y = x^3

    plt.show() #Comando necessário para poder printar o gráfico


# ---------------------------------------------------FORMATO DA CURVA-------------------------------------------------------------------------------------------------------------------------------


def gráfico_cores_formadoDeCurva():
    x = np.linspace(0, 2, 21)
    plt.plot(x, x, 'b--')   # linha azul (b) 
                            # tracejada (--)
    plt.plot(x, x**2, 'go--') # verdes (g)
                            # bolinhas (o) 
                            # linhas tracejadas
    plt.plot(x, x**3, 'r^') # vermelhos (r)
                            # nenhuma linha 
                            # triângulos (^)
    plt.show()


#------------------------------------DETALHES----------------------------------------------------------------------------------------------------------------------------------------------------


# LEGENDAS (parâmetro label, função legend) para cada curva
# TÍTULO no gráfico (title)
# DESCRIÇÕES nos eixos coordenados (xlabel e ylabel) 
# GRADE para facilitar a leitura do gráfico (grid):

def grafico_com_introducao_de_legendas_nas_curvas_e_eixos():
    x = np.linspace(0, 2, 21)
    plt.plot(x, x, 'b--', label='linear')        # linear é a legenda da curva

    plt.plot(x, x**2, 'go', label='quadrático')  # quadrático é a legenda da curva

    plt.plot(x, x**3, 'r^', label='cúbico')      # cúbico é a legenda da curva

    plt.xlabel('teste x')                        # 'teste x' é o nome dado ao eixo x

    plt.ylabel('teste y')                        # 'teste y' é o nome dado ao eixo y

    plt.title('Gráfico simples')                 # 'Gráfico simples' é o nome do gráfico

    plt.legend()#comando que habilita as legendas do gráfico

    plt.grid()  #Adiciona um quadriculado ao gráfico

    plt.show()

#--------------------------------------Legendas em pontos específicos do gráfico----------------------------------------------------------------------------------------------------------

def grafico_com_introducao_de_legendas_em_pontos_especificos():
    # Dados para o gráfico
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 1, 3, 5]

    # Crie um gráfico de dispersão
    plt.scatter(x, y)

    # Adicione anotações em pontos específicos do gráfico com a função "annotate". 

    #COMO USAR: annotate(s, xy, xytext=None, xycoords='data', textcoords='data', arrowprops=None, **kwargs)
    """
    s: É a string de texto que você deseja anotar no gráfico. 
    xy: É uma tupla representando as coordenadas do ponto que você está anotando. Por exemplo, xy=(x, y) especifica as coordenadas do ponto no gráfico.
    xytext: (Opcional) É uma tupla que representa a posição onde o texto da anotação deve ser colocado. Se não for especificado, o texto será colocado nas coordenadas xy.
    xycoords: (Opcional) É a coordenada do sistema de referência para xy. O valor padrão é 'data', que significa que xy se refere às coordenadas de dados do gráfico. Você pode usar outras opções, como 'axes fraction', 'figure points', entre outras, dependendo do sistema de coordenadas desejado.
    textcoords: (Opcional) É a coordenada do sistema de referência para xytext. O valor padrão é 'data', que significa que xytext se refere às coordenadas de dados do gráfico. Você pode usar outras opções, como 'axes fraction', 'figure points', entre outras, dependendo do sistema de coordenadas desejado.
    arrowprops: (Opcional) É um dicionário com propriedades da seta que conecta o ponto anotado ao texto da anotação. Você pode personalizar a aparência da seta, como estilo, cor, largura, entre outros, usando este dicionário.
    **kwargs: (Opcional) Outros argumentos de palavras-chave podem ser usados para personalizar a aparência do texto da anotação, como tamanho da fonte, cor do texto, entre outros.
    """

    plt.annotate('Ponto 1', (1, 2), textcoords='offset points', xytext=(10,10), arrowprops=dict(arrowstyle='->'))
    plt.annotate('Ponto 2', (2, 4), textcoords='offset points', xytext=(10,10), arrowprops=dict(arrowstyle='->'))
    plt.annotate('Ponto 3', (3, 1), textcoords='offset points', xytext=(10,10), arrowprops=dict(arrowstyle='->'))
    plt.annotate('Ponto 4', (4, 3), textcoords='offset points', xytext=(10,10), arrowprops=dict(arrowstyle='->'))
    plt.annotate('Ponto 5', (5, 5), textcoords='offset points', xytext=(10,10), arrowprops=dict(arrowstyle='->'))

    # Exibir o gráfico
    plt.show()



#Para adicionar limites aos eixos dos gráfcos de forma personalizada, é usada a função "xlim(limite inicial, limite final)" para x e "ylim(limite inicial, limite final)" para y 


def grafico_com_eixos_limitados():
    x = np.linspace(0, 21, 100) #vai usar um intervalo de 0 a 21 com 100 pontos
    a = np.linspace(0, 21) #vai usar um intervalo de 0 a 21 com 100 pontos

    plt.plot(x, x**2, label='quadrático')  
    plt.plot(a, a**2 + 2, label='quadrático')  

    plt.xlabel('teste x') 

    plt.xlim(0, 21) #coloca um limite de 0 a 21 no eixo x

    plt.ylabel('teste y') 

    plt.ylim(0, 21) #coloca um limite de 0 a 21 no eixo x

    plt.title('Gráfico simples')            
    plt.legend()
    plt.grid()
    plt.show()


# ---------------------------------------------------PARA DEIXAR OS EIXOS EM ESCALA É USADA A FUNÇÃO "AXIS" ------------------------------------------------------------------------------

# Essa função vai receber os parametros "xminimo","xmáximo" e "yminimo","ymáximo"
# Configura os limites dos eixos x e y
# exemplo : plt.axis([0, 6, 0, 6])
# ""xminimo" = 0, "xmáximo" = 6 e "yminimo" = 0,"ymáximo" = 6"


def grafico_em_escala():
    xmin = 0
    ymin = 0
    xmax = 21
    ymax = 21

    x = np.linspace(0, 21, 100) #vai usar um intervalo de 0 a 21 com 100 pontos
    a = np.linspace(0, 21) #vai usar um intervalo de 0 a 21 com 100 pontos

    plt.plot(x, x**2, label='quadrático')  
    plt.plot(a, a**2 + 2, label='quadrático')  

    plt.xlabel('teste x') 

    #plt.xlim(0, xmax + 2) #coloca um limite de 0 a 21 no eixo x

    plt.ylabel('teste y') 

    #plt.ylim(0, ymax + 2) #coloca um limite de 0 a 21 no eixo x

    plt.axis([xmin, xmax, ymin, xmax])

    plt.title('Gráfico simples')            
    plt.legend()
    plt.grid()
    plt.show()

def grafico_de_barras(rótulos, valores, título='Gráfico de Barras', xlabel='Categorias', ylabel='Valores'):
    """
    Cria um gráfico de barras.

    Parâmetros:
    rótulos (list): Lista de rótulos para as barras.
    valores (list): Lista de valores correspondentes aos rótulos.
    título (str): Título do gráfico.
    xlabel (str): Nome do eixo x.
    ylabel (str): Nome do eixo y.
    """
    
    plt.bar(rótulos, valores, color='skyblue')
    plt.title(título)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis='y')
    plt.show()
    # Exemplo de uso da função
    # rótulos = ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D']
    # valores = [10, 15, 7, 12]
    # grafico_de_barras(rótulos, valores)


#-----------------------------------------------------------------COLOCANDO MAIS DE UM GRÁFICO EM UMA FIGURA-------------------------------------------------------------------------------------

#Para usar mais de um gráfico em uma mesma figura é usado a função "figure". Ela vai pedir alguns parametros 

