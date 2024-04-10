matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

print("Matriz:")
for valor in matriz:
    print(valor)

soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if j > i:
           matriz[i][j] = 0

print("Matriz:")
for valor in matriz:
    print(valor)
