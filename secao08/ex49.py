import random

def criar_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = [random.randint(1, 20) for _ in range(colunas)]
        matriz.append(linha)
    return matriz

def soma_abaixo_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j < i:
                soma += matriz[i][j]
    return soma

matriz = criar_matriz(3, 3)

print("Matriz:")
for linha in matriz:
    print(linha)

print(f'A soma dos numeros abaixo da diagonal principal é de : {soma_abaixo_diagonal(matriz)}')
