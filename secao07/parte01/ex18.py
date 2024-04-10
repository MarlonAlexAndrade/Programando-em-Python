import random

lista = random.sample(range(1, 10), 9)
print(f'Lista gerada: {lista}')

numero = int(input("Digite um numero: "))

for i in lista:
    if numero % i == 0:
        print(i)
        