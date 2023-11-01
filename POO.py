# --------------------------------------------------POO com python-------------------------------------------------------------------------

#Objeto = Classe

#O objeto tem métodos (ações) e atributos (informações)

#Quando a classe é construida, as funções internas a essa classe são métodos e as informações dessas funções são os atributos.

#Ex: O objeto "Pessoa" consegue fala, andar, pular, dormir... Essas ações seriam os métodos dentro da classe. 
#    "Pessoa" também tem idade, cpf, nome, aniversário... Esses seriam os atributos da classe "Pessoa". Atribultos também podem ser variáveis dentro do código.

#------------------------------------------------VANTAGENS-----------------------------------------------------------------------------------------

"""
Encapsulamento: Protege o código de mudanças indesejadas. 
    Ex: Para o objeto "TV", não dá para desligar a tv no botão de aumentar volume.

Herança: As instancias do objeto tem valores diferentes mas com as mesmas caracteristicas. 
    Ex: cor de um objeto carro pode ser branca ou vermelha. "cor" é a herança. 

Polimorfismo: Uma mesma classe pode conter outras classes dentro dela. 
    Ex: Uma classe "Animal" pode conter uma classe "gato" e "cachorro" dentro dela.
"""

#------------------------------------------------CRIANDO A PRIMEIRA CLASSE--------------------------------------------------------------------------------------------------------------

"""
Primeiro passo é nomear a classe.
Segundo passo é inicializar a classe com a função def __init__(self):
Terceiro passo é definir os atributos que essa classe vai ter quando iniciar.
""" 

class Televisao: #classe televisão criada
    def __init__(self): #iniciando com a função __init__
        self.marca = 'LG'    #atributo marca recebe "LG"
        self.tamanho = 55    #atributo marca recebe "55"
        self.cor = 'Preta'   #atributo marca recebe "Preta"
        self.canal = 'Globo' #atributo marca recebe "Globo"

#Quando a classe for atribuida a uma variável, ela vai iniciar com todos os atributos listados.

televisao_sala = Televisao()   #instancia do objeto Televisão (sala)
televisao_quarto = Televisao() #instancia do objeto Televisão (quarto)
# "televisao_sala" e "Televisao_quarto" herdam as caracteristicas da classe televisão (Herança) 
#  print(televisao_sala.marca) #saida será: LG


#-------------------------------------------------MODIFICANDO ATRIBUTOS INICIAIS EM UMA CLASSE------------------------------------------------------------------------------------


# Quando o comando "OBJETO.ATRIBUTO = ALGUMA_COISA" é execultado, o objeto que tem o "ATRIBUTO" é modificado para "ALGUMA_COISA"
# Ex:

televisao_sala.marca = 'Dell' # Objeto "televisao_sala" que tem o atributo "marca" foi modificado para "Dell"
print(televisao_sala.marca)   # Saída será "Dell"


#--------------------------------------------------------------------------SELF---------------------------------------------------------------------------------------------------------------

#self é uma convenção usada para se referir ao próprio objeto de uma classe. Ele permite que outros métodos dentro da classe manipulem dados específicos. 
#Quando o self é atribuido a uma def, ela vai mudar dados dentro da' classe. Para inserir mais dados dentro da def é necessário adicionar mais parâmetros.


class Televisao: #classe televisão criada
    def __init__(self): #iniciando com a função __init__
        self.marca = 'LG'    #atributo marca recebe "LG"
        self.tamanho = 55    #atributo marca recebe "55"
        self.cor = 'Preta'   #atributo marca recebe "Preta"
        self.canal = 'Globo' #atributo marca recebe "Globo"

    def mudar_canal(self, novo_canal): # Essa def é responsável por criar a funcionalidade na TV de mudar o canal sem usar o comando "televisao_sala.canal = 'Dell'"
        self.canal = novo_canal        # Esse self vai referenciar ao atributo que está na função "__init__"

    def desligar(self):#Essa def poderia ser colocada no "__init__", mas é introduzida como uma funcionalidade específica.
        print("A TV está desligada.")
        self.estado = "desligada"      # Adicionando um novo atributo "estado" específico para a instância

# Criando uma instância da classe Televisao
minha_tv = Televisao()

# Acessando atributos da instância
print(f"Marca da TV: {minha_tv.marca}")
print(f"Tamanho da TV: {minha_tv.tamanho} polegadas")
print(f"Cor da TV: {minha_tv.cor}")
print(f"Canal atual: {minha_tv.canal}")

# Mudando o canal com o método mudar_canal
minha_tv.mudar_canal("CNN") #Quando a função é chamada, é como se o self fosse um parâmetro a menos e só é necessário colocar o novo canal.
print(f"Novo canal atual: {minha_tv.canal}")

# Desligando a TV com o método desligar
minha_tv.desligar()

# Tentando acessar o atributo "estado" após desligar
# Isso resultará em um erro, pois o atributo "estado" não foi definido no método __init__
# e é específico para a instância
print(f"Estado da TV: {minha_tv.estado}")
#Se você deseja acessar o atributo "estado" em todas as instâncias, mesmo antes de chamar o método desligar, você deve definir esse atributo no método __init__ com um valor padrão, 
#conforme mostrado no exemplo anterior. Dessa forma, o atributo "estado" estará presente em todas as instâncias da classe desde o início.

















































































































































































#Exercício do slide de POO de Sergio

class Aluno:
    def __init__ (self):
        self.cpf = 0
        self.nome = ''
        self.nota1 = 0 
        self.nota2 = 0
        self.nota3 = 0
        """
    def inicializarNota(self, nota, numeroProva)
        self.nota1 = 
        self.nota2 = 
        self.nota3 = 
    def verificarSituacaoMedia(nota, numeroProva)
        nota1 = 
        nota2 = 
        nota3 = 
        """
