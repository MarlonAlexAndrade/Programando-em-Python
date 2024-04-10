import random

def criar_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = [random.randint(1, 20) for _ in range(colunas)]
        matriz.append(linha)
    return matriz

def transpor_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz_transposta[j][i] = matriz[i][j]

    return matriz_transposta

matriz = criar_matriz(3, 3)
matriz_transposta = criar_matriz(3, 3)

print("Matriz:")
for linha in matriz:
    print(linha)

print(transpor_matriz(matriz))
