def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial


def soma_algarismos(numero):
    if numero > 0:
        soma = 0
        while numero != 0:
            resto = calcular_fatorial(numero) % 10
            numero = (calcular_fatorial(numero) - resto) // 10
            soma += resto

        return soma
    else:
        return "Número inválido..."

numero = int(input('Digite um número: '))

print(f'A soma dos dígitos é: {soma_algarismos(numero)}')