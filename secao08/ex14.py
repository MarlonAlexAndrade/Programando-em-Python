def calculo_consumo(km, litro):
    km_litro = km / consumo

    if km_litro < 8:
       return "Venda o carro!"
    elif km_litro > 8 and km_litro < 12:
        return "Econômico"
    elif km_litro > 12:
       return "Super Econômico"
    else:
        return "Retorne um valor válido!"

km = int(input("Digite a quantidade de quilometros pecorridos: "))
consumo = int(input("Digite a quantidade de gasolina consumida: "))

print(calculo_consumo(km, consumo))
