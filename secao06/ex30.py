def soma_primeiros_naturais(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

def soma_alternada(n):
    soma = 0
    sinal = 1
    for i in range(1, 2*n, 2):
        soma += sinal * i
        sinal *= -1
    return soma

def soma_impares(n):
    soma = 0
    for i in range(1, 2*n, 2):
        soma += i
    return soma

# Teste das funções
n = int(input("Digite um valor inteiro para n: "))
print("Soma dos primeiros", n, "números naturais:", soma_primeiros_naturais(n))
print("Soma da sequência 1 - 2 + 3 - 4 + ... + (2n - 1):", soma_alternada(n))
print("Soma dos números ímpares até", 2*n - 1, ":", soma_impares(n))
