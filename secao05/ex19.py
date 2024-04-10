def divisibilidade(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return (f"{numero} é divisível por 3 e por 5 ao mesmo tempo")
    elif numero % 3 == 0:
        return (f"{numero} é divisível por 3, mas não por 5")
    elif numero % 5 == 0:
        return (f"{numero} é divisível por 5, mas não por 3")
    else:
        return (f"{numero} não é divisível nem por 3 nem por 5")

numero = int(input("Digite um número: "))
print(divisibilidade(numero))