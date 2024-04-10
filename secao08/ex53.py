def soma_acima_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j > i:
                soma += matriz[i][j]
    return soma
def soma_abaixo_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j < i:
                soma += matriz[i][j]
    return soma

def soma_diagonal_principal(matriz):
    soma = 0
    for linha in range(len(matriz)):      
        for coluna in range(len(matriz)):
            if coluna == linha:
                soma += matriz[linha][coluna]
    return soma

def matriz_identidade(matriz):
    if soma_abaixo_diagonal(matriz) != 0:
        return "Não é uma matriz identidade"
    elif soma_acima_diagonal(matriz) != 0:
        return "Não é uma matriz identidade"
    elif soma_diagonal_principal(matriz) != len(matriz):
        return "Não é uma matriz identidade"
    elif soma_diagonal_principal(matriz) == len(matriz):
        return "É uma matriz identidade"


matriz = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

print("Matriz:")
for linha in matriz:
    print(linha)

print(matriz_identidade(matriz))
