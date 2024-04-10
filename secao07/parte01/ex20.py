import random

lista = random.sample(range(0, 50), 10)
print(f'Lista gerada: {lista}')

impares = []

for i in lista:
    if i % 2 != 0:
        impares.append(i)

print("Elementos da lista:")
for i in lista:
    print(i)

print("\n Números ímpares:")
for x in impares:
    print(x)