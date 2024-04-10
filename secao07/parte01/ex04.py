vetor = [1, 0, 5, 2, 5, 7, 5, 3]

posicao01 = int(input("Digite a primeira posição: "))
posicao02 = int(input("Digite a segunda posição: "))

for i in range(0, 8):
    print(vetor[i])


soma = vetor[posicao01] + vetor[posicao02]
print(f'A soma dos valor da posicao {posicao01} e da posicao {posicao02} é de {soma}')
