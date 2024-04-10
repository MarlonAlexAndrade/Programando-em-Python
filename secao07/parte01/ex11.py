import random

lista = random.sample(range(-10, 10), 10)
print(f'Lista gerada: {lista}')

soma = 0
contador = 0

for num in lista:
    if num >= 0:
        soma += num
    else:
        contador += 1

print(f'A quantidade de numeros negativos é de {contador} e a soma dos numeros positivos é de {soma}')