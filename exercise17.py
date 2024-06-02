# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 23:15:32 2022

@author: luisb
"""

diccionario = { 
    

    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifthteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    30:"thirty",
    40:"forty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety",
    100:"hundred",
    1000:"thousand",
    0:"and"

    }

valores = 0

for i in range(1,1001):
    
    if i <=  20:
        
        a = len(list(diccionario[i]))
        
        print(list(diccionario[i]))
        
        valores += a
        
    elif(i == 1000):
        
        valores += len(list(diccionario[i]))  + len(list(diccionario[i/1000]))
        
        print(len(list(diccionario[i]))  ,len(list(diccionario[i/1000])))
        
        a = i/1000  
        
    elif(20<i<100):
        
        a = i//10
        
        b = (i - a*10)
        
        if b == 0:
            
            valores += len(list(diccionario[a*10]))
            
            print(list(diccionario[a*10]))
            
            
            
        else:
            valores += len(list(diccionario[a*10])) +  len(list(diccionario[b]))
        
            print(list(diccionario[a*10]),list(diccionario[b]))
    else:
        
        a = i//100 
        b = (i - a*100)//10
        c = (i - a*100 - b*10)
        
        
        if c == 0 and b == 0:
            
            valores += len(list(diccionario[a])) + len(list(diccionario[100]))
            
            print(list(diccionario[a]),list(diccionario[100]))
             
            
        elif c == 0:
            
            valores += len(list(diccionario[a])) + len(list(diccionario[100])) + len(list(diccionario[0])) +len(list(diccionario[b*10]))
           
            print(list(diccionario[a]),list(diccionario[100]), list(diccionario[0]), list(diccionario[b*10]))
             
            
        elif b == 0:
            
            valores += len(list(diccionario[a])) + len(list(diccionario[100])) + len(list(diccionario[0])) + len(list(diccionario[c]))
            
            print(list(diccionario[a]),list(diccionario[100]),list(diccionario[0]),list(diccionario[c]))
            
        else:
            
            valores += len(list(diccionario[a])) + len(list(diccionario[100])) + len(list(diccionario[0])) +len(list(diccionario[b*10]))+len(list(diccionario[c]))
           
            print(list(diccionario[a]),list(diccionario[100]), list(diccionario[0]), list(diccionario[b*10]),list(diccionario[c]))
        
        
        
        
        
print(valores)
        
        
        
        