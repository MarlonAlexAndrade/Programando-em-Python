def calculo(numero01, numero02, sinal):
    if sinal == '+':
        soma = numero01 + numero02
        return soma
    elif sinal == '-':
        subtração = numero01 - numero02
        return subtração
    elif sinal == '/':
        divisao = numero01 / numero02
        return divisao
    elif sinal == '*':
        multiplicação = numero01 * numero02
        return multiplicação
    else:
        return "Esse não é um numero valido!"
    
numero01 = float(input("Digite o primeiro numero: "))
numero02 = float(input("Digite o segundo numero: "))
sinal = input("Digite o sinal, para executar o calculo Exp: +: ")

print(calculo(numero01, numero02, sinal))
