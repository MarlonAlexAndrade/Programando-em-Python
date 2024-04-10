import random

def criar_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = [random.randint(1, 20) for _ in range(colunas)]
        matriz.append(linha)
    return matriz

def soma_diagonal_secundaria(matriz):
    soma = 0
    contador = len(matriz)-1

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j == contador:
                soma += matriz[i][j]
        contador -= 1

    return soma

matriz = criar_matriz(3, 3)

print("Matriz:")
for linha in matriz:
    print(linha)

print(f'A soma dos numeros acima da diagonal principal é de : {soma_diagonal_secundaria(matriz)}')
