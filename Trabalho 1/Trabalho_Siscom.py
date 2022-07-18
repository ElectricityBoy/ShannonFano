'''
UNIVERSIDADE FEDERAL DA BAHIA
DISCENTE: ELDER DOS SANTOS GUEDES PEREIRA
DISCIPLINA: SISTEMAS DE COMUNICAÇÃO I
DOCENTE: LETICIA 
                    IMPLEMENTAÇÃO DO MÉTODO DE SHANNON FANO PARA COMPRESSÃO DE DADOS
'''

from collections import Counter
import numpy as np
import operator
import pandas as pd

class ShanonFanno(object):

    def __init__(self):
        self.sorted_s = []
        self.char_dict = dict()
        self.encoded_dict = dict()
        self.encoded_string = ''

        
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
                    
                

    def make_count(self):
        self.char_dict = dict(Counter(self.sentence))
        char_ls = sorted(self.char_dict.items(), key=operator.itemgetter(1),reverse=True)
        sorted_s = []
        for i in char_ls :
            sorted_s.append(i[0])
        return self.char_dict, sorted_s

    

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

    

    def dataset(self, s):
        x = np.array(self)
        table = dict()
        
        for i in s:
            table[i]= s.count()
        df = pd.DataFrame(list(table.items()),columns = ['Símbolos','Frequência'])
        print(df)
    
    
        
        
    def display_compressed(self):
        print("-="*20)
        print("A palavra codificada é:")
        for ch in self.sentence:
            print(self.encoded_dict[ch], end="")
        print("\n")
    


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
shf = ShanonFanno()
shf.encode(word)
shf.display_compressed()
