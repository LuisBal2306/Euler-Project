# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 17:39:46 2022

@author: luisb
"""

f = open("exercise13.txt", "r")
lineas = f.readlines()

suma=0

for i in lineas:
    
    suma += int(i)

f.close()

#Solución 5537376230
