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

"""

#O primeiro passo é gerar os valores de x que serão usados; aqui, usamos a função "linspace" do numpy. Em seguida graficamos as funções com a função plot e executamos o comando plt.show() para mostrar o gráfico na tela:
x = np.linspace(0, 2, 21) # 21 pontos no intervalo [0, 2]
plt.plot(x, x)            # função y = x

plt.plot(x, x**2)         # função y = x^2

plt.plot(x, x**3)         # função y = x^3

plt.show() #Comando necessário para poder printar o gráfico


# -----------------------------------FORMATO DA CURVA--------------------------------------------------------

"""

"""

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

"""

#------------------------------------DETALHES-----------------------------------------------------------------------------------------------------------


# LEGENDAS (parâmetro label, função legend) para cada curva
# TÍTULO no gráfico (title)
# DESCRIÇÕES nos eixos coordenados (xlabel e ylabel) 
# GRADE para facilitar a leitura do gráfico (grid):

"""

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

"""

#Para adicionar limites aos eixos dos gráfcos de forma personalizada, é usada a função "xlim(limite inicial, limite final)" para x e "ylim(limite inicial, limite final)" para y 

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
