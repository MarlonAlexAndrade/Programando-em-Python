import math

termos = 5  
s = 0       

for i in range(termos):
    denominador = math.factorial(2*i)  
    s += i / denominador               

print("O valor da série para", termos, "termos é:", s)
