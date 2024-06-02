# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 21:34:55 2022

@author: luisb

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

"""

#Nota: Al correr el programa falta una secuencia, no encuentro cual es la que falta.

maneras = []
x=0
contador = 0

for i in range(0,201,1):

    x = i
    j=0
    k=0
    l=0
    m=0
    n=0
    o=0
    p=0
    
    if x < 200:
        for j in range(0,201,2):  
            x = i + j
            if x<200:
                for k in range(0,201,5):
                    x = i + j + k
                    if x<200:
                        for l in range(0,201,10):
                            x = i + j + k + l
                            if x<200:
                                for m in range(0,201,20):
                                    x = i + j + k + l + m
                                    if x<200:
                                        for n in range(0,201,50):
                                            x = i + j + k + l + m + n
                                            if x<200:
                                                for o in range(0,201,100):
                                                    x = i + j + k + l + m + n + o
                                                    if x<200:
                                                        for p in range(0,201,200):
                                                            x = i + j + k + l + m + n + o + p
                                                            if x == 200:
                                                                contador+=1
                                                                print(x, i,j,k,l,m,n,o, p,contador)
                                                                
                                                                break
                                                            else:
                                                                break
                                                    elif x==200:
                                                        contador+=1
                                                        print(x, i,j,k,l,m,n,o, p,contador)
                                                        
                                                        break
                                                    else:
                                                        break
                                            elif x==200:
                                                contador+=1
                                                print(x, i,j,k,l,m,n,o, p,contador)
                                                
                                                break
                                            else:
                                                break
                                    elif x==200:
                                        contador+=1
                                        print(x, i,j,k,l,m,n,o,p,contador)
                                        
                                        break
                                    else:
                                        break
                                        
                            elif x==200:
                                contador+=1
                                print(x, i,j,k,l,m,n,o, p,contador)
                                
                                break
                            else:
                                break         
                    elif x==200:
                        contador+=1
                        print(x, i,j,k,l,m,n,o, p,contador) 
                        
                        break
                    else:
                        break
            elif x == 200:
                contador+=1
                print(x, i,j,k,l,m,n,o, p,contador)   
                
                break
            else:
                break
    elif x== 200:
        contador+=1
        print(x, i,j,k,l,m,n,o, p,contador)
        
        break
              
    else:
        break


"""
# We use the standard dynamic programming algorithm to solve the subset sum problem over integers.
# The order of the coin values does not matter, but the values need to be unique.
def compute():
	TOTAL = 200
	
	# At the start of each loop iteration, ways[i] is the number of ways to use {any copies
	# of the all the coin values seen before this iteration} to form an unordered sum of i
	ways = [1] + [0] * TOTAL
	for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
		for i in range(len(ways) - coin):
			ways[i + coin] += ways[i]
	return str(ways[-1])


if __name__ == "__main__":
	print(compute())          
            
"""    
    
    
        
        
        
        
        
        
        
  
    