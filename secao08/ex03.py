def verificacao(numero):
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    elif numero == 0:
        return 0
    
numero = int(input("Digite o numero: "))
print(verificacao(numero))
