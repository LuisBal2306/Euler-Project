#fibonacci serie, encuentra el indice de la serie de fibo que contenga 1000 dí­gitos

a = 0
b = 1

x=0
i=0

while (x/pow(10,999))<1:

        total = a+b
        b=a
        a=total
        print(i+1)
        
        x = total
        
        i+=1

print(total)

#resultado = 4782

