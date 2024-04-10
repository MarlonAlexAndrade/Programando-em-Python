matriz = [[7, 2, 3], [5, 6, 7], [9, 10, 11]]

print("Matriz:")
for valor in matriz:
    print(valor)

soma = 0
contador = len(matriz)-1

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if j == contador:
            soma += matriz[i][j]
    contador -= 1

print(f'Soma dos elementos da diagonal secundaria: {soma}')
