#Importando as bibliotecas necessárias para a criação do código
import numpy as np
import pandas as pd
from binarytree import Node
import sys
import os
import math
#Criando uma função para identificar os simbolos únicos da palavra de entrada
def unique(list1):
    x = np.array(list1)

#Recebendo a palavra/frase do usuário
word = list(input('Insira uma palavra/frase: ' ))
#Criando uma variavel chamada simbolos com as letras únicas presentes na palavra recebida
simbolos = unique(word)
table = dict()
for i in word:
    table[i]= word.count(i)
#Criando um dataframe com os dados
df = pd.DataFrame(list(table.items()),columns = ['Simbolos','Frequência']) 
total = sum(table.values())
df['P(i)'] = df['Frequência']/total

#Passo 2 
df = df.sort_values(by=['Frequência'], ascending=False).reset_index()
#--------------------------
#Dividindo em grupos
probabilidades = list(df['P(i)'])

