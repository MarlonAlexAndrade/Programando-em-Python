matriz = [[7, 2, 3], [5, 6, 7], [9, 10, 11]]

print("Matriz:")
for valor in matriz:
    print(valor)

for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz[0])):
        soma += matriz[j][i] 
    print({soma})
