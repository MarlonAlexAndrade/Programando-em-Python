matriz = [[1] * 3 for _ in range(3)]

print("Matriz:")
for valor in matriz:
    print(valor)

soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if j == i:
            soma += matriz[i][j]

print(f'Soma dos elementos da diagonal principal: {soma}')
