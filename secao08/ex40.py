import random

def numero_pares(vetor):
    contador = 0
    for valor in vetor:
        if valor % 2 == 0:  
            contador += 1
    return contador

vetor = [random.randint(1, 50) for _ in range(10)]

print(vetor)

print(f'O número de pares é de {numero_pares(vetor)}')
