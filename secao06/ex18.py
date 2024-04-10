numero = 1
maior_numero = float('-inf')
menor_numero = float('inf')

while numero != 0:
    numero = int(input("Digite um numero: "))

    if numero > maior_numero:
        maior_numero = numero
        qtd_maior = 1
    elif numero == maior_numero:
        qtd_maior += 1

    if numero < menor_numero:
        menor_numero = numero
        qtd_menor = 1
    elif numero == menor_numero:
        qtd_menor += 1


    print(f'O maior numero é {maior_numero}, e foi lido {qtd_maior}')
    print(f'O menor numero é {menor_numero}, e foi lido {qtd_menor}')
