def simplifica(numerador, denominador):
    for i in range(2, min(numerador, denominador) + 1):
        while numerador % i == 0 and denominador % i == 0:
            numerador //= i
            denominador //= i
    return numerador, denominador

numerador = int(input("Digite o numerador: "))
denominador = int(input("Digite o denominador: "))

simplificado_numerador, simplificado_denominador = simplifica(numerador, denominador)
print(f'A fração simplificada é: {simplificado_numerador}/{simplificado_denominador}')
