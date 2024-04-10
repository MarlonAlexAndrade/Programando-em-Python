import random

lista = random.sample(range(0, 50), 10)
print(f'Lista gerada: {lista}')

lista01 = []
lista02 = []

for valor in lista:
    if valor % 2 == 0:
        lista02.append(valor)
    else:
        lista01.append(valor)

print(f'Lista pares: {lista02}')
print(f'Lista ímpares: {lista01}')
