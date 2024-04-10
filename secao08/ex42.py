import random

def numero_pares(vetor):
    soma = 0
    for valor in vetor:
        soma += valor    
        media = soma / len(vetor)
    return media
vetor = [random.randint(1, 50) for _ in range(10)]

print(vetor)

print(f'A media dos numeros é de {numero_pares(vetor)}')
