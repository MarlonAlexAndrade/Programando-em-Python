lista01 = [1, 2, 3, 4, 5]
lista02 = [1, 2, 3, 4, 5]

escalar = 0

for x, y in zip(lista01, lista02):
    escalar += x * y

print(f'O resultado do produto escalar é de {escalar}')
