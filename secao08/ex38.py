def fatorial_exponencial(numero):
    fe = 0
    for i in range(1, numero + 1):
        fe +=  i**-i
    return fe

numero = int(input("Digite um número inteiro: "))

print(fatorial_exponencial(numero))
