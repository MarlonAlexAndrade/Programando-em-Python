import random

lista = random.sample(range(1, 30), 10)
print(f'Lista gerada: {lista}')

pares = []
impares = []

for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f' O numero de pares digitado é de {len(pares)} e a soma é de {sum(pares)}')
print(f' O numero de impares digitado é de {len(impares)} e a soma é de {sum(impares)}')
