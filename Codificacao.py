#Importing some libraries
import numpy as np
import pandas as pd

#Creating a function to separate unique simbols from a string
def unique(list1):
    x = np.array(list1)

#Receiving a word list
word = list(input('Insira uma palavra/frase: ' ))
#Creating a variable with unique values
simbolos = unique(word)
table = dict()
for i in word:
    table[i]= word.count(i)
#Creating a dataframe
df = pd.DataFrame(list(table.items()),columns = ['Simbolos','Frequência']) 
total = sum(table.values())
df['P(i)'] = df['Frequência']/total

#Step 2 
df = df.sort_values(by=['Frequência'], ascending=False).reset_index()

#Slice in groups
probabilidades = list(df['P(i)'])
simbols = list(df['Simbolos'])

#Find the middle index


def middle(lists):
    a = True
    index = 0
    while a == True:
        soma = probabilidades[index]
        if round(soma) == round(sum(probabilidades[index:])):
            a = False
        else:
            index+=1
        if index == len(probabilidades):
            break
    return(index)
    
middlep = middle(probabilidades)

group1= probabilidades[:middlep]
group2 = probabilidades[middlep:]
code1 = [0] * len(group1)
code2 = [1] * len(group2)
def g1(lists):
    code4 = [0] * len(lists)
    a = middle(lists)
    t1,t2 = group1[:a],group2[a:]
    for i in range(len(t1)-1):
        if t1[i] >= t1[i+1]:
            code4[i] = str(code4[i]) + '0'
            for x in code4[i+1:]:
                code4[code4.index(x)]  =  str(code4[code.index(x)]) + '1'
    return(code4)

def g2(lists):
    a = middle(lists)
    code3 = [1] * len(lists)
    t1,t2 = group1[:a],group2[a:]
    for i in range(len(t1)-1):
        if t1[i] >= t1[i+1]:
            code3[i] = str(code3[i]) + '0'
            for x in code3[i+1:]:
                code3[code3.index(x)]  =  str(code3[code3.index(x)]) + '1'
    return(code3)


for i in range(len(group1)-1):
    if group1[i] >= group1[i+1]:
        code1[i] = str(code1[i]) + '0'
        for x in code1[i+1:]:
           code1[code1.index(x)]  =  str(code1[code1.index(x)]) + '1'

for j in range(len(group2)-1):
    if group2[j] >= group2[j+1]:
        code2[j] = str(code2[j]) + '0'
        for x in code2[j+1:]:
           code2[code2.index(x)]  =  str(code2[code2.index(x)]) + '1'
           
code = code1 + code2

df['Code'] = code

print(df)
print(g2(group2))



           

