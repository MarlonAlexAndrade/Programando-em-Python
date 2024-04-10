def calcular_serie(N):
    soma = 0
    for i in range(1, N + 1):
        termo = ((i ** 2) + 1) / (i + 3)
        soma += termo
    return soma

N = int(input("Digite o valor de N: "))
resultado = calcular_serie(N)

print("O resultado da série é:", resultado)
