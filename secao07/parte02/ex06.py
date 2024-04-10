matriz01 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matriz02 = [[2, 4, 6, 3], [4, 5, 6, 7], [8, 5, 10, 11], [16, 17, 14, 12]]
matriz03 = []

print("Matriz01:")
for valor in matriz01:
    print(valor)

print("Matriz02:")
for valor in matriz02:
    print(valor)

maior = float('-inf')

for i in range(len(matriz01)):
    for j in range(len(matriz02)):
        if matriz01[i][j] > matriz02[i][j]:
            matriz03.append(matriz01[i][j])
            
        elif  matriz02[i][j] > matriz01[i][j]:
            matriz03.append(matriz02[i][j])

    print(matriz03)
    