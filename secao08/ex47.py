import random

def criar_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = [random.randint(1, 100) for _ in range(colunas)]
        matriz.append(linha)
    return matriz

def maior_que_dez(matriz):
    contador = 0
    for linha in matriz:
        for valor in linha:
            if valor > 10:
                contador += 1
    return contador

matriz = criar_matriz(4, 4)

print("Matriz:")
for linha in matriz:
    print(linha)

print(f"A quantidade de números acima de 10 na matriz é: {maior_que_dez(matriz)}")
