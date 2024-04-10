numero = int(input("Digite um numero: "))

primos = 0
x = 1
soma = 0

if numero < 2 : 
    print("Digite um numero maior que 1")   
else:
    while primos < numero:
        x += 1
        if x % 2 != 0:
            primos += 1
            soma += x
            print(x)

   
    print(f'A soma dos primos ate n é de {soma}')