maior_numero = float('-inf')
menor_numero = float('inf')

for i in range(0, 10):
    num = int(input("Digite um numero: "))

    if num < menor_numero:
        menor_numero = num
    if num > maior_numero:
        maior_numero = num

print(f'O maior numero é {maior_numero} e o menor é {menor_numero}')
