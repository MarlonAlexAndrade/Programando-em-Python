import random

def criar_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = [random.randint(1, 20) for _ in range(colunas)]
        matriz.append(linha)
    return matriz

def soma_acima_diagonal(matriz):
    soma = 0
    for linha in range(len(matriz)):      
        for coluna in range(len(matriz)):
            if coluna > linha:
                soma += matriz[linha][coluna]
    return soma

matriz = criar_matriz(3, 3)

print("Matriz:")
for linha in matriz:
    print(linha)

print(f'A soma dos numeros acima da diagonal principal é de : {soma_acima_diagonal(matriz)}')
