linhas = int(input("Digite a quantidade de linhas na matriz: "))
colunas = int(input("Digite a quantidade de colunas na matriz: "))

matriz = [[0] * colunas for _ in range(linhas)]

for i in range(linhas):
    for j in range(colunas):
        numero = int(input(f"Digite o número para a posição [{i}][{j}]: "))
        matriz[i][j] = numero

print("Matriz:")
for linha in matriz:
    print(linha)

maior = float('-inf')
linha_maior = 0
coluna_maior = 0

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_maior = i
            coluna_maior = j

print(f'O maior número é {maior}, localizado na linha {linha_maior} e coluna {coluna_maior}.')
