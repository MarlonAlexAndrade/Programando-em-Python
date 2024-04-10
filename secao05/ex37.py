hora_entrada = int(input("Digite a hora de entrada: "))
minutos_entrada = int(input("Digite os minutos de entrada: "))

hora_saida = int(input("Digite a hora da saida: "))
minutos_saida = int(input("Digite os minutos de saida: "))

horas_totais = hora_saida - hora_entrada
minutos_totais = minutos_saida - minutos_entrada

if minutos_totais != 0 and minutos_totais > 0:
    horas_totais += 1

if horas_totais == 1 :
    print("O valor do estacionamento ficara R$1.00")
elif horas_totais == 2:
    print("O valor do estacionamento ficara R$1.00")
elif horas_totais == 3:
    print("O valor do estacionamento ficara R$1.40")
elif horas_totais == 4:
    print("O valor do estacionamento ficara R$1.40")
elif horas_totais >= 5:
    print(f'O valor do estacionamento ficara {((horas_totais - 4) * 2) + 4.8}')
