def somatoria(numero):
    soma = 0
    for i in range(numero):
        soma += i
    
    return soma

numero = int(input("Digite o numero: "))

print(somatoria(numero))
