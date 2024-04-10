matriz01 = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
matriz02 = [[12, 13, 14], [15, 16, 17], [18, 19, 29]]
matriz03 = [[0] * 3 for _ in range(3)]

for i in range(len(matriz01)):
    for j in range(len(matriz02)):
        matriz03[i][j] = matriz01[i][j] * matriz02[i][j]

print("Matriz:")
for valor in matriz03:
    print(valor)
