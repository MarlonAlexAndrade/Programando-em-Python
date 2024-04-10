numero = int(input("Digite um numero: "))

primos = 1


if numero < 2 : 
    print("Digite um numero maior que 1")   
else:
    while primos < numero:
        primos += 1
        if primos % 2 != 0:
            print(primos)
    