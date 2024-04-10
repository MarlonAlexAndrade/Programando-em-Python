import random

lista = random.sample(range(0, 15), 15)
print(f'Lista gerada: {lista}')

for i in lista:
    if i == 0:
        index = lista.index(i)
        lista.remove(i)
        
for i in range(0, 14):
    print(lista)
    