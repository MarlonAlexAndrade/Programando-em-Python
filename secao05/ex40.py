custo_fabrica = int(input("Digite o valor de fabrica do carro: "))

custo_consumidor = 0

if custo_fabrica < 12000:
    custo_consumidor = custo_fabrica * 1.05
elif custo_fabrica >= 12000 and custo_fabrica <= 25000:
    custo_consumidor = custo_fabrica * 1.25
elif custo_fabrica > 25000:
    custo_consumidor = custo_fabrica * 1.35

print(f'O custo para o consumidor é de {custo_consumidor}')