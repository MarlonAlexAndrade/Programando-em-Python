matriz = [[7, 2, 3], [5, 6, 7], [9, 10, 11]]
matriz_transposta = []

print("Matriz:")
for valor in matriz:
    print(valor)

for i in range(len(matriz)):
    matriz_transposta.append([0] * len(matriz[0]))

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz_transposta[j][i] = matriz[i][j]

print("Matriz Transposta:")
for valor in matriz_transposta:
    print(valor)
