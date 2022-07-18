#Importando bibliotecas 
from collections import Counter # Importação de uma ferramenta utilizado para realizar contagens de maneira mais rápida e prática
import numpy as np # Implementação de vetores
import operator # Utilização dos operadores intrínsecos da linguagem para utilização da orientação a objetos
import pandas as pd #Biblioteca para criação de dataframe
import math #Biblioteca para operações matematicas. Nesse trabalho foi utilizado para calcular o Log em especifico

#Função para calcular a entropia
def entropy(args=[]):
  entropy = 0
  for p, l in zip(args, map(lambda i: math.log(i, 2), args)):
    entropy += p*l
  return -entropy

#Função para descofificar a string

def decode(encoded_string, dictionary):
    holder = []
    codes = list(dictionary.values())
    symbols = list(dictionary.keys())
    inv_dictionary = dict(zip(codes, symbols))
    while(len(encoded_string) != 0):
        for code in codes:
            if encoded_string.startswith(code):
                holder.append(inv_dictionary.get(code))
                encoded_string = encoded_string[len(code):]
    return holder
#Criando uma classe chamada ShannonFano para a realização do método

class Shannon_Fano(object):
    #Contrutor da classe para a designação dos parametros utilizaods
    def __init__(self):
        self.sorted_s = []
        self.char_dict = dict()
        self.encoded_dict = dict()
        self.encoded_string = ''

    #Função para a leitura do dicionario e construção da árvore   
    def code_tree(self, symbols):
        if len(symbols)==2:
            self.encoded_dict[symbols[0]] += '0'
            self.encoded_dict[symbols[1]] += '1'
        elif len(symbols)>2:
            breaking_index = self.break_the_node(symbols)
            for i in range(len(symbols)):
                left_part = i<=breaking_index
                if left_part:
                    self.encoded_dict[symbols[i]] += '0'
                else:
                    self.encoded_dict[symbols[i]] += '1'
            self.code_tree(symbols[:breaking_index+1])
            self.code_tree(symbols[breaking_index+1:])
                    
                
    #Função para fazer a contagem dos caracteres da string
    def make_count(self):
        self.char_dict = dict(Counter(self.sentence))
        char_ls = sorted(self.char_dict.items(), key=operator.itemgetter(1),reverse=True)
        sorted_s = []
        for i in char_ls :
            sorted_s.append(i[0])
        return self.char_dict, sorted_s

    
    #Função para identificar quando a árvore deverá parar de ser ramificada
    def break_the_node(self, node):
        total = 0
        for i in range(len(node)):
            total += self.char_dict[node[i]]
        length = len(node)
        count = 0
        last_char_index = 0
        for i in range(length):
            count += self.char_dict[node[i]]
            if (count - (total/2) < 0):
                last_char_index += 1
        return last_char_index

    
    #Função para criação da tabela e exibição dos resultados
    def table(self,s):
        x = np.array(s)
        table = dict()
        
        for i in s:
            table[i]= s.count(i)

        df = pd.DataFrame(list(table.items()),columns = ['Símbolos','Frequência'])
        total = sum(table.values())
        df['P(i)'] = df['Frequência']/total
        df = df.sort_values(by=['Frequência'], ascending=False).reset_index()
        df['Codificação']  = list(self.encoded_dict.values())

        print("-="*20)
        print(df)
        print("-="*20)
        print('A entropia calculada é: ',entropy(list(df['P(i)'])))
    
      
    #Função para exibição da palavra codificada  
    def compressed(self):
        print("-="*20)
        print("A palavra codificada é:")
        codeword = ''
        for ch in self.sentence:
            codeword += self.encoded_dict[ch]

        print(codeword,'\n')
        print("-="*20)
        print("A palavra decodificada é:")
        return decode(codeword,self.encoded_dict) #Retorna a palavra decodificada
    
      

    #Implementação de um dicionario com os respectivos caracteres e seus códigos gerados
    def encode(self, s):
        self.sentence = s
        self.total = len(s)
        self.char_dict, self.sorted_s = self.make_count() 
        self.encoded_dict = {new_list: '' for new_list in self.sorted_s}
        self.code_tree(self.sorted_s)
        for ch in self.sentence:
            self.encoded_string += self.encoded_dict[ch]
        return self.encoded_string
      

word = list(input('Insira uma palavra/frase: ' ))
shf = Shannon_Fano()
shf.encode(word)
shf.table(word)
shf.compressed()