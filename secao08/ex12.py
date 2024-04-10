def soma_algarismos(numero):
    if numero > 0:
        soma = 0
        while numero != 0:
            resto = numero % 10
            numero = (numero - resto) // 10
            soma += resto

        return soma
    else:
        return "Número inválido..."

numero = int(input('Digite um número: '))

print(f'A soma dos dígitos é: {soma_algarismos(numero)}')