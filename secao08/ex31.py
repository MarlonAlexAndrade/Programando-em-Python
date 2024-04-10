def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial


def numero_neperiano(numero):
    resultado = 0
    for i in range(numero):
        resultado += 1 / calcular_fatorial(i)

    return resultado

numero = int(input("Digite um numero: "))
print(numero_neperiano(numero))
