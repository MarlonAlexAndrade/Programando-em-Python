numero = int(input("Digite um numero inteiro: "))

fatorial = 1
i = 1

if numero <= 0:
    print("Digite um numero valido!")
else:
    while i <= numero:
        fatorial *= i 
        i += 1

print(fatorial)