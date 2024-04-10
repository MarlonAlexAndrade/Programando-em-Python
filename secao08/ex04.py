def quadrado_perfeito(numero):
    if numero > 0:
        return numero**2
    else:
        return "Não é um quadrado perfeito"
    
numero = int(input("Digite o numero: "))
print(quadrado_perfeito(numero))
