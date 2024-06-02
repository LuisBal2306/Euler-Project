# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 16:53:36 2022

@author: luisb
"""


def divisores(value):
    
    divisores = []
    
    for i in range(1,value+1):
        
        if value % i == 0 :
            
            divisores.append(i)
            
    return(divisores)

for i in range(0,1000000):
    
    x = divisores(i)
    
    if len(x) == 6:
        
        print(x)
        
   
        
        