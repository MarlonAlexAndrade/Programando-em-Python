numero = int(input("Digite um numero: "))

i = 1
soma = 0

if numero > 0:
    for i in range(i, numero):
        if numero % i == 0:
            soma += i
else:
    print("Digite um numero valido!")

print(f'A soma dos divisores é de {soma}')