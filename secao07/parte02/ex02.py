matriz = []

for i in range(0, 5):
    matriz.append([0] * 5)

posicao01 = 0
for i in range(0, 5):
    matriz[i][posicao01] = 1
    posicao01 += 1
    
print(matriz)
