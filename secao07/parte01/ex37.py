import random

lista = random.sample(range(1, 20), 11)
print(f'Lista gerada: {lista}')

indice = 6

lista[:indice] = sorted(lista[:indice])

lista[indice:] = reversed(lista[indice:])

print(f'Lista ordenada e invertida: {lista}')
