hora_inicio = int(input("Digite a hora: "))

minuto_inicio = int(input("Digite os minutos: "))

segundos_inicio = int(input("Digite os segundos: "))

duracao = int(input("Digite a duração da experiencia em segundos: "))

horas_totais = int(duracao / 3600)
minutos_totais = int((duracao % 3600) / 60)
segundos_totais = int((duracao % 3600) % 60)  

minutos_finais = 0
horas_finais = 0

segundos_finais = segundos_inicio + segundos_totais
if segundos_finais >= 120:
    segundos_finais -= 120
    minutos_finais += 2
elif segundos_finais >= 60:
    segundos_finais -= 60
    minutos_finais += 1

minutos_finais += minuto_inicio + minutos_totais
if minutos_finais >= 60:
    minutos_finais -= 60
    horas_finais += 1

horas_finais += hora_inicio + horas_totais

print(f'A hora final será {horas_finais}h{minutos_finais}m {segundos_finais}s')