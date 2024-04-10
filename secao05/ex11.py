numero = int(input('Digite um número: '))

if numero > 0:
    soma = 0

    while numero != 0:
        resto = numero % 10
        numero = (numero - resto) // 10
        soma += resto
else:
    print('Número inválido...')

print(f'A soma dos dígitos é: {soma}')
