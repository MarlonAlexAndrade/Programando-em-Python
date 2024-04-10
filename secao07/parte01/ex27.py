import random

lista01 = random.sample(range(0, 50), 10)
print(f'Lista gerada: {lista01}')

primo = []

for i in lista01:
    if i % 2 != 0:
        primo.append(i)
    
for i in primo:
    print(f'O numero {primo} é primo e seu index é {primo.index(i)}')
