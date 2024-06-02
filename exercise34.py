# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 07:56:54 2022

@author: luisb
"""

def factorial(x): 
    
    factorial = 1
    
    for i in range(1,x+1):
        
        factorial = factorial * i 
        
    return factorial

arreglo = []

for i in range(100000000):
    
    a = i//100000000
    j = i-100000000*a
    b = j//10000000
    k = j-10000000*b
    c = k//1000000
    l = k-1000000*c
    d = l//100000
    m = k-100000*d
    e = l//10000
    m = k-10000*e
    f = m//1000
    o = k-1000000*c
    g = l
    
    if a == 0:
        if b  == 0:
            if c == 0:
                suma = factorial(d)
            else:
                suma = factorial(c)+factorial(d)
        else:
            suma = factorial(b)+factorial(c)+factorial(d)
    else:
        suma = factorial(a)+factorial(b)+factorial(c)+factorial(d)    
                
            
                
    
    suma = factorial(a)+factorial(b)+factorial(c)+factorial(d)
    
    #print(i,a,b,c,d,suma)
    
    if suma == i+1:
        
        print(i)
    
    
    