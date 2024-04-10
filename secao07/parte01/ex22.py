import random

lista01 = random.sample(range(0, 50), 10)
print(f'Lista gerada: {lista01}')

lista02 = random.sample(range(0, 50), 10)
print(f'Lista gerada: {lista02}')

lista03 = []

for i in range(len(lista01)):
    if i % 2 == 0:
        lista03.append(lista01[i]) 
    else:
        lista03.append(lista02[i])

print(f'Lista combinada: {lista03}')
