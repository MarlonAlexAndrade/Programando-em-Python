import random

def criar_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = [random.randint(1, 20) for _ in range(colunas)]
        matriz.append(linha)
    return matriz

def produto_matricial(matriz01, matriz02):
    linhas_matriz01 = len(matriz01)
    colunas_matriz01 = len(matriz01[0])
    colunas_matriz02 = len(matriz02[0])

    matriz03 = [[0 for _ in range(colunas_matriz02)] for _ in range(linhas_matriz01)]

    for i in range(linhas_matriz01):
        for j in range(colunas_matriz02):
            for k in range(colunas_matriz01):
                matriz03[i][j] += matriz01[i][k] * matriz02[k][j]

    return matriz03

matriz01 = criar_matriz(3, 2)
matriz02 = criar_matriz(2, 3)

print("Matriz01:")
for linha in matriz01:
    print(linha)

print("Matriz02:")
for linha in matriz02:
    print(linha)

print("Produto Matricial:")
resultado = produto_matricial(matriz01, matriz02)
for linha in resultado:
    print(linha)
