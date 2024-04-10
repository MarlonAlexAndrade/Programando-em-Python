import random

inicio_intervalo = 1
fim_intervalo = 100
quantidade_numeros = 25

numeros_gerados = []
cartela_bingo = []

while len(numeros_gerados) < quantidade_numeros:
    numero_aleatorio = random.randint(inicio_intervalo, fim_intervalo)
    if numero_aleatorio not in numeros_gerados:
        numeros_gerados.append(numero_aleatorio)

for _ in range(5):
    linha = []
    for _ in range(5):
        linha.append(0)  
    cartela_bingo.append(linha)

for i in range(5):
    for j in range(5):
        cartela_bingo[i][j] = numeros_gerados.pop(0)  

print("\nCartela bingo:")
for valor in cartela_bingo:
    print(valor)
