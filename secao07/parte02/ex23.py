matriz01 = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
matriz02 = [[0] * 3 for _ in range(3)]

for i in range(len(matriz01)):
    for j in range(len(matriz02)):
        matriz02[i][j] = matriz01[i][j] **2

print("Matriz:")
for valor in matriz02:
    print(valor)
