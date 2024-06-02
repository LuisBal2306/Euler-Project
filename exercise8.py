# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 15:49:01 2022

@author: luisb


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

def raizexacta(num):
    
    if num**(1/2) == int(num**(1/2)):
        
        
        return True
        
    else: 
        
        return False
    
        


for a in range(0,1000):
    
    for b in range (0,1000):
        
        calcuadrado = a**2 + b**2 
        
        x = raizexacta(calcuadrado)
        
        if x == True:
            
            if a + b + calcuadrado**(1/2) == 1000 :
                
                print(a,b,calcuadrado,a*b*calcuadrado**(1/2))


















