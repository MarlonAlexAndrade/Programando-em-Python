n = int(input(f'Digite o número de linhas: '))

imprimir = 1
for i in range(1, n + 1):
    for i in range(1, i + 1):
        print(f'{imprimir:<4}', end='')
        imprimir += 1
    print()
