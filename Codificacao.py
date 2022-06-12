#Importing some libraries
import numpy as np
import pandas as pd
import math

#Creating a function to separate unique simbols from a string
def unique(list1):
    x = np.array(list1)

#Creating a function to calculate the entropy
def calculate_entropy(args=[]):
    entropy = 0
    for p, l in zip(args, map(lambda i: math.log(i, 2), args)):
        entropy += p*l
    return -entropy

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

group1,simbols1= probabilidades[:middlep],simbols[:middlep]
group2,simbols2 = probabilidades[middlep:],simbols[middlep:]
code1 = [0] * len(group1)
code2 = [1] * len(group2)
code = {}
for i in simbols1:
    code[i] = code1[simbols1.index(i)]
for j in simbols2:
    code[j] = code2[simbols2.index(j)]



out = []
out.append(probabilidades)
count = 0
temp = []


for i in range(len(probabilidades)+1):
    a = middle(out[i])
    if (a == 2 and len(out)==1) or (a ==2 and len(out)>1):
        out.append(out[i][:a])
        temp.append(out[i][a:])
        out.pop(0)
        break
    else:
        out.append(out[i][:a])
        temp.append(out[i][a:])
    

for j in range(len(temp)):
    count +=1
    a = middle(temp[i])
    if (a==2 and len(temp[i])==2) or (a==2 and len(temp)>1):
        break
    else:
        temp.append(temp[i][:a])
        temp.append(temp[i][a:])
print(out)


def g1(lists):
    code4 = [0] * len(lists)
    a = middle(lists)
    t1,t2 = group1[:a],group2[a:]
    for i in range(len(t1)-1):
        if t1[i] >= t1[i+1]:
            code4[i] = str(code4[i]) + '0'
            for x in code4[i+1:]:
                code4[code4.index(x)]  =  str(code4[code4.index(x)]) + '1'
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




'''
code = g1(group1) + g2(group2) 

df['Code'] = code



print('=-'*20)
print(df)
print('=-'*20)
print('The entropy is: ',calculate_entropy(probabilidades))
print(g1(group1))


'''
           

