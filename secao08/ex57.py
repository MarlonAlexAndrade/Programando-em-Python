import random

def criar_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = [random.randint(1, 20) for _ in range(colunas)]
        matriz.append(linha)
    return matriz

def soma_coluna(matriz, posicao):
    soma = 0
    for j in range(len(matriz)):
        soma += matriz[j][posicao]
    return soma

posicao = int(input("Digite a coluna que deseja somar: "))

matriz = criar_matriz(7, 6)

print("Matriz:")
for linha in matriz:
    print(linha)

print(f'A soma dos numeros na coluna é de: {soma_coluna(matriz, posicao)}')
