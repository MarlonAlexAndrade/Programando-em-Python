import random

lista01 = random.sample(range(0, 50), 10)
print(f'Lista gerada: {lista01}')

lista02 = random.sample(range(0, 50), 10)
print(f'Lista gerada: {lista02}')


lista03 = set(lista01) - set(lista02)
print(f'Lista gerada: {lista03}')

