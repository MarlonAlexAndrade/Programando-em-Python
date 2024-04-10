segundos = int(input("Digite o a quantidade de segundos: "))

horas_totais = segundos / 3600
minutos_totais = (segundos % 3600) / 60
segundos_totais = (segundos % 3600) % 60 

print(f'Numero de horas é de {int(horas_totais)}h {int(minutos_totais)}m {int(segundos_totais)}s')
