matriz = [[7, 2, 3, 5, 4, 8], [5, 6, 7, 5 , 7, 2], [9, 10, 11, 9, 7, 4]]
nova_matriz = []

soma = 0
media = 0
contador = 0

print("Matriz:")
for valor in matriz:
    print(valor)

for linha in range(len(matriz)):
    soma_coluna = 0
    nova_linha = []
    for coluna in range(len(matriz[0])):
        if coluna % 2 != 0:
            soma += matriz[linha][coluna]
        
        if coluna == 1 or coluna == 3: 
            media += matriz[linha][coluna]
            contador += 1

        if coluna == 1 or coluna == 2:  
            soma_coluna += matriz[linha][coluna]
        nova_linha.append(matriz[linha][coluna])
    nova_linha.append(soma_coluna)  
    nova_matriz.append(nova_linha)

print(f'Soma dos elementos nas colunas ímpares: {soma}')
print(f'A média aritmética da segunda e quarta colunas é de: {media / contador}')

print("Nova Matriz:")
for valor in nova_matriz:
    print(valor)
