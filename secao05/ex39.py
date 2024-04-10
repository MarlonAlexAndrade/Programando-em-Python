
valor_salario = float(input("Digite o salario do funcionario: "))
tempo_servico = int(input("Digite o tempo de serviço do funcionario: "))

if valor_salario > 0 and tempo_servico >= 0:
    if valor_salario <= 500 and tempo_servico < 1:
        novo_salario = valor_salario * 1.25
    elif valor_salario <= 1000  and tempo_servico <= 3:
        novo_salario = valor_salario * 1.20 + 100
    elif valor_salario <= 1500  and tempo_servico <= 6:
        novo_salario = valor_salario * 1.15 + 200
    elif valor_salario <= 2000  and tempo_servico <= 10:
        novo_salario = valor_salario * 1.10 + 300
    elif valor_salario > 2000  and tempo_servico > 10:
        novo_salario = valor_salario  + 500   
    else:
        novo_salario = valor_salario
    print(f'O salario do funcionário será de {novo_salario}')
else:
    print("Valores inválidos fornecidos.")
