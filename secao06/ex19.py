import random

numero = random.randint(100, 999)

print(numero)
ultimo = numero // 1 % 10
print(ultimo)
meio = numero // 10 % 10
print(meio)
primeiro = numero // 100 % 10
print(primeiro)
