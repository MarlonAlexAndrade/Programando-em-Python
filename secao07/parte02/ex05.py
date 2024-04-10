linhas = int(input("Digite a quantidade de linhas na matriz: "))
colunas = int(input("Digite a quantidade de colunas na matriz: "))

matriz = [[0] * colunas for _ in range(linhas)]

for i in range(linhas):
    for j in range(colunas):
        numero = int(input(f"Digite o número para a posição [{i}][{j}]: "))
        matriz[i][j] = numero

print("Matriz:")
for valor in matriz:
    print(valor)

x = int(input("Digite o valor que deseja procurar: "))

linha = None
coluna = None
for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] == x:
            linha = i
            coluna = j
            print(f'O numero {x} esta na linha {linha} e na coluna {coluna}')
            
if linha == None and coluna == None:
    print("Não encontrado!")          