import random

lista = random.sample(range(-10, 10), 10)
print(f'Lista gerada: {lista}')

for i in lista:
    if lista[i] < 0:
        lista[i] = 0

print(lista)
