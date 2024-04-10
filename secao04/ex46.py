numero = input("Digite um numero de tres digitos maior que 99 e menor que 1000: ")

numero_invertido = numero[::-1]

if(int(numero) > 99 and int(numero) < 1000):
    print(numero_invertido)
else:
    print("Não é um numero valido!")