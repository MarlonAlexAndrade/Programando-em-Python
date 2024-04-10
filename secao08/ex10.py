def maior_numero(numero01, numero02):
    if numero01 > numero02:
        return numero01
    elif numero02 > numero01:
        return numero01
    else:
        return "Empate"
    
numero01 = int(input("Digite o primeiro numero: "))
numero02 = int(input("Digite o segundo numero: "))

print(maior_numero(numero01, numero02))
