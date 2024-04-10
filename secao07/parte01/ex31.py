import random

lista01 = random.sample(range(1, 15), 10)
print(f'Lista gerada: {lista01}')

lista02 = random.sample(range(1, 15), 10)
print(f'Lista gerada: {lista02}')

union = set(lista01) | set(lista02)

print(union)
