lista = []

maior = float('-inf')
menor = float('inf')

for i in range(0, 10):
    altura = float(input("Digite a sua altura: "))

    lista.append(altura)

    if i > maior:
        maior = max(lista)
        index_maior = lista.index(maior)
    elif i < menor:
        menor = min(lista)
        index_menor = lista.index(menor)
    
print(f'O aluno mais alto é o aluno {index_maior} e sua altura é de {maior} ')
print(f'O aluno mais baixo é o aluno {index_menor} e sua altura é de {menor} ')   
