import random

def maior_valor(vetor):
    maior = float('-inf')
    for valor in vetor:
        if valor > maior:  
            maior = valor
    return maior

vetor = [random.randint(1, 50) for _ in range(10)]

print(vetor)

print(f'O maior valor é  {maior_valor(vetor)}')
