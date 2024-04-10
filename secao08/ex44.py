import random

def separar(vetor):
    vetor_pares = []
    vetor_impares = []
    for valor in vetor:
        if valor % 2 == 0:
            vetor_pares.append(valor)
        elif valor % 2 != 0:
            vetor_impares.append(valor)
    return vetor_pares, vetor_impares

vetor = [random.randint(1, 100) for _ in range(30)]

print(separar(vetor))
