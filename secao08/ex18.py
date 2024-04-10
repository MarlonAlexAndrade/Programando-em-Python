def exponenciacao(numero, expoente):
    resultado = numero**expoente
    
    return resultado

numero = int(input("Digite um numero: "))
expoente = int(input("Digite o seu expoente: "))

print(exponenciacao(numero, expoente))
