def fatorial_duplo(numero):
    if numero > 0 and numero % 2 != 0:
        fatorial = 1  
        for i in range(1, numero + 1):  
            if i % 2 != 0:
                fatorial *= i
        return fatorial
    else:
        return "O número não é ímpar ou é negativo!"

numero = int(input("Digite um número ímpar e positivo: "))
print(fatorial_duplo(numero))
