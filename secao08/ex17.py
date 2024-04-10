def soma_intermediarios(numero01, numero02):
    soma = 0

    if numero01 < numero02:
        for i in range(numero01 + 1, numero02):
            soma += i
    else:
        for i in range(numero02 + 1, numero01):
            soma += i

    return soma

numero01 = int(input("Digite um número de início: "))
numero02 = int(input("Digite um número de fim: "))

print(soma_intermediarios(numero01, numero02))
