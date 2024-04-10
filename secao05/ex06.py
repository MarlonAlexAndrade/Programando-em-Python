num01 = int(input("Digite o primeiro numero: "))

num02 = int(input("Digite um segundo numero: "))

if num01 > num02:
    diferenca = num01 - num02
    print(f'O maior numero é {num01}')
    print(f'A diferença entre eles é de {diferenca}')
else:
    diferenca = num02 - num01
    print(f'O maior numero é {num02}')
    print(f'A diferença entre eles é de {diferenca}')
    