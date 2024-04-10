import random

lista01 = random.sample(range(1, 15), 5)
print(f'Lista gerada: {lista01}')

lista02 = random.sample(range(1, 15), 5)
print(f'Lista gerada: {lista02}')



for x, y in zip(lista01, lista02):
    soma = x + y
    produto = x * y
    intersecao = [valor for valor in lista01 if valor in lista02]
    uniao = set(lista01) | set(lista02)

    print(f'A soma é de {soma}')
    print(f'O produto é de {produto}')


print(f'A intersecao é {intersecao}')
print(f'A união das taelas é {uniao}')
