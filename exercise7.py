# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 20:38:40 2022

@author: luisb

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
that the 6th prime is 13.

What is the 10 001st prime number?

"""

primos = [2]
i = 3

while len(primos)<10001:
    
    for j in range(2,i):
        
        if i%j == 0:
            
            #print(i,j)
            
            break
        
        if j==i-1:
            
            #print(i)
            
            primos.append(i)
        
    
    i+=1

#Solución: 104743
        
    
    







