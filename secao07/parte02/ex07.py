matriz = [[1] * 10 for _ in range(10)]

print("Matriz:")
for valor in matriz:
    print(valor)

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i < j:
            matriz[i][j] = 2*i + 7*j - 2
        elif i == j:
            matriz[i][j] = 3*i**2 - 1
        elif i > j:
            matriz[i][j] = 4*i**3 - 5*j**2 + 1

print("Matriz:")
for valor in matriz:
    print(valor)
