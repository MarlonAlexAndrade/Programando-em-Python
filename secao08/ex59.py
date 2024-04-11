import random

def uniao_vetores(vetor01, vetor02):
    vetor03 = set(vetor01) | set(vetor02)

    return vetor03

vetor1 = [random.randint(1, 100) for _ in range(10)]
vetor2 = [random.randint(1, 100) for _ in range(10)]

print(f'Vetor 1: {vetor1}')
print(f'Vetor 2: {vetor2}')
print(f'A união dos vetores é de {uniao_vetores(vetor1, vetor2)}')
