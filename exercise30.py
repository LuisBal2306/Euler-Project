# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 20:26:20 2022

@author: luisb

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""

"""
#Convertir a cadena
parseo = str(number)

#convertir cadena a entero
cadena= "1"
numero= int(cadena)

"""

total = 0

for i in range(2,100000):
    
    suma = 0
    
    #8560
    
    x = i
    
    e = x//10000
    
    x = x-10000*e
    
    a = x//1000
    
    x = x-1000*a
    
    b = x//100
    
    x = x-100*b
    
    c = x//10
    
    x = x-10*c
    
    d = x
      
    #print(i,a,b,c,d)
    
    lista = [e,a,b,c,d]
    
    #print(i,lista)
    
    for j in lista:
        
        suma += pow(j,5)
        
    if suma == i:
        
        print(i)
        
        total += i
        


    
