vetor = []
pares = 0

for i in range(0, 11):
    vetor.append(i)
    
    if vetor[i] % 2 == 0:
        pares += 1 

print(f'O vetor possui {pares} numeros pares')