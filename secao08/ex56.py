import random

def criar_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = [random.randint(1, 20) for _ in range(colunas)]
        matriz.append(linha)
    return matriz

def soma_linha(matriz, posicao):
    soma = 0
    for j in range(len(matriz[posicao])):
        soma += matriz[posicao][j]
    return soma

posicao = int(input("Digite a linha que deseja somar: "))

matriz = criar_matriz(7, 6)

print("Matriz:")
for linha in matriz:
    print(linha)

print(f'A soma dos numeros na linha é de: {soma_linha(matriz, posicao)}')
