base = int(input("Digite a base do triangulo: "))
altura = int(input("Digite a altura do triangulo: "))


if base <= 0 or altura  < 0:
    print("Digite um numero valido: ")

else:
    area = (base * altura) / 2
    print(f'A area do triangulo é de {area}')
    