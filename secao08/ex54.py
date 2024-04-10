import random

def criar_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = [random.randint(1, 20) for _ in range(colunas)]
        matriz.append(linha)
    return matriz

def soma_matriz(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            soma += matriz[i][j]
    return soma

matriz = criar_matriz(4, 4)

print("Matriz:")
for linha in matriz:
    print(linha)

print(f'A soma dos elementos da matriz é de: {soma_matriz(matriz)}')
