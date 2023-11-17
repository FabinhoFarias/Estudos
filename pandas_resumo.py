import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Usando barra dupla no caminho do arquivo
caminho_do_arquivo = 'Python/Resultados_simulado.csv'

# Ou usando barra invertida no estilo Unix
# caminho_do_arquivo = 'C:/Users/FABINHO/Desktop/Códigos/Resultado_simulado.csv'

dataFrame = pd.read_csv(caminho_do_arquivo)

#print(dataFrame)

coluna_nomes = np.array(dataFrame['Nome'])
coluna_linguagens = np.array(dataFrame['Linguagens '])
coluna_mat = np.array(dataFrame['Matemática'])
coluna_nt = np.array(dataFrame['Natureza'])
coluna_human = np.array(dataFrame['Humanas'])





soma_mat = coluna_mat.sum()/len(coluna_mat)
#print(soma_mat)






def notas (array_nomes, array_notas):
    array_nomes = np.array(array_nomes)
    metade_Nomes = array_nomes[0:int(len(array_nomes)/4)]
    metade_Notas = array_notas[0:int(len(array_notas)/4)]
    plt.xticks(range(len(metade_Nomes)), metade_Nomes, rotation=45, ha='right')

    array_notas = np.array(array_notas)
    plt.plot(metade_Nomes, metade_Notas, 'r^')
    plt.show()
#print(coluna_mat)

notas(coluna_nomes, coluna_mat)
