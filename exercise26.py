# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 18:20:27 2022

@author: luisb
"""

x = 0

for i in range(2,10):
    
    x = 1/i
    
    print(x*10000000)
    
    
    while type(x*10) == (int):
        
        x = x*10
        
        print(x,type(x*10))