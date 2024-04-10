import random

lista = random.sample(range(0, 15), 10)
print(f'Lista gerada: {lista}')

for i in range(len(lista) - 1):
   for j in range(len(lista) -1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)