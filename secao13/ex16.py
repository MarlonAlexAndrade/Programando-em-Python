import random

vetor = [random.randint(1, 100) for _ in range(10)]

with open('ex16.txt', 'w') as arq:
    for numero in vetor:
        arq.write(f'{numero:b}\n')
