def logaritmo_base_10(numero):  
        expoente = 0
        while numero >= 10:
            numero /= 10
            expoente += 1
        return expoente


numero = int(input("Digite um numero inteiro: "))

if numero < 0:
    print("Número Invalido!")
else:
    resultado = logaritmo_base_10(numero)
    print("O logaritmo de", numero, "na base 10 é:", resultado)



