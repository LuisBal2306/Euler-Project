# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 21:30:28 2022

@author: luisb

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

primos = [2]

i = 0
suma = 2

while i<2000000:
   
    for j in range(2,i):
        
        if i%j == 0:
            
            #print(i,j)
            
            break
        
        if j==i-1:
            
            #print(i)
            
            primos.append(i)
            
            suma += i
            
    i+=1
    
#Solución necesita muchos recursos
        

