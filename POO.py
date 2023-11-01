
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

televisao_sala = Televisao()

# print(televisao_sala.marca) #saida será: LG













#-------------------------------------------------MODIFICANDO ATRIBUTOS INICIAIS EM UMA CLASSE------------------------------------------------------------------------------------









































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
