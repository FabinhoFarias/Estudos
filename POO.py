#------------------------------------------------POO com python-------------------------------------------------------------------------

# Em Python toda variável aponta para um objeto. 
# Podem ser de 2 tipos: PRIMITIVOS: São variáveis, floots, int...
#                       COMPOSTOS: Listas, dicionários, classes...


#Objeto = Classe

#O objeto tem métodos (ações) e atributos (informações)

#Quando a classe é construida, as funções internas a essa classe são métodos e as informações dessas funções são os atributos.

#Ex: O objeto "Pessoa" consegue fala, andar, pular, dormir... Essas ações seriam os métodos dentro da classe. 
#    "Pessoa" também tem idade, cpf, nome, aniversário... Esses seriam os atributos da classe "Pessoa". Atribultos também podem ser variáveis dentro do código.

#------------------------------------------------VANTAGENS----------------------------------------------------------------------------------------------------------------

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
Segundo passo é inicializar a classe com a função def __init__(self): #Este método de inicialização é também chamado de construtor.
                                                                      Ele é chamado automaticamente sempre que um objeto da
                                                                      classe é criado/instanciado.#
Terceiro passo é definir os atributos que essa classe vai ter quando iniciar.
""" 

class Televisao: #classe televisão criada
    def __init__(self): #iniciando com a função __init__
        self.marca = 'LG'    #atributo marca recebe "LG"
        self.tamanho = 55    #atributo marca recebe "55"
        self.cor = 'Preta'   #atributo marca recebe "Preta"
        self.canal = 'Globo' #atributo marca recebe "Globo"

#Quando a classe for atribuida a uma variável, ela vai iniciar com todos os atributos listados.

televisao_sala = Televisao()   # instancia do objeto Televisão (sala)
televisao_quarto = Televisao() # instancia do objeto Televisão (quarto)
                               # Cada objeto instanciado é diferente do outro.
# "televisao_sala" e "Televisao_quarto" herdam as caracteristicas da classe televisão (Herança) 
#  print(televisao_sala.marca) #saida será: LG


#------------------------------------------------MODIFICANDO ATRIBUTOS INICIAIS EM UMA CLASSE------------------------------------------------------------------------------------


# Quando o comando "OBJETO.ATRIBUTO = ALGUMA_COISA" é execultado, o objeto que tem o "ATRIBUTO" é modificado para "ALGUMA_COISA"
# Ex:
televisao_sala.marca = 'Dell' # Objeto "televisao_sala" que tem o atributo "marca" foi modificado para "Dell"
print(televisao_sala.marca)   # Saída será "Dell"

"""
Nosso construtor também pode inicializar as variáveis da classe com valores fornecidos no momento da criação do objeto:
"""
class Pessoa:
    def __init__(self, initNome, initIdade, initEndereco): # coloca-se o init + nome do atributo com inicial maiúscula. Ex: "initAtributo"
        self.nome = initNome
        self.idade = initIdade
        self.endereco = initEndereco        

p1 = Pessoa("João Pedro da Silva", 20, "Rua Sem Nome") # p1 iniciará com nom = "João Pedro da Silva", idade = 20 e endereco = "Rua Sem Nome"
p2 = Pessoa("Maria Xuxa", 47, "Rua da Nave Espacial")  # p2 iniciará com nom = "Maria Xuxa", idade = 47 e endereco = "Rua da Nave Espacial"

print(p1.nome) #saida = João Pedro da Silva
print(p2.nome) #saida = Maria Xuxa


#------------------------------------------------SELF---------------------------------------------------------------------------------------------------------------

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



#------------------------------------------------EM_RESUMO---------------------------------------------------------------------------------------------------------------



# Atributo: um campo de informação dentro de uma classe (por exemplo, endereco, idade, nome na classe Pessoa)
class Pessoa:
    # Classe: um tipo composto definido pelo usuário.
    def __init__(self, initNome, initIdade, initEndereco):
        # Construtor: inicializa um objeto de sua classe.
        # Instancia um objeto de sua classe. Cria um objeto de sua classe.
        self.nome = initNome
        self.idade = initIdade
        self.endereco = initEndereco

# Instância: um objeto cujo tipo é uma classe. Instância é sinônimo de objeto.

# Exemplo de uso:
# Criando instâncias (objetos) da classe Pessoa
p1 = Pessoa("João Pedro da Silva", 20, "Rua Sem Nome")
p2 = Pessoa("Maria Xuxa", 47, "Rua da Nave Espacial")
# Acessando os atributos das instâncias
print(p1.nome)
print(p2.nome)




#------------------------------------------------BOAS_PRÁTICAS---------------------------------------------------------------------------------------------------------------


# PROTEGER ATRIBUTOS: Evite que os atributos sejam acessados (lidos e escritos) diretamente por quem está FORA de sua classe.
# Isso permite que se tenha controle do protocolo de mudança de valores de seus atributos









































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

 
