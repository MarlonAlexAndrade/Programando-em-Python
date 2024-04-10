km = int(input("Digite a quantidade de quilometros pecorridos: "))
consumo = int(input("Digite a quantidade de gasolina consumida: "))

km_litro = km / consumo

if km_litro < 8:
    print("Venda o carro!")
elif km_litro > 8 and km_litro < 12:
    print("Econômico")
elif km_litro > 12:
    print("Super Econômico")
