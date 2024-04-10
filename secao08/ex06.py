def conversor_segundos(horas, minutos, segundos):
    horas *= 3600
    minutos *= 60
    return horas + minutos + segundos

horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

print(conversor_segundos(horas, minutos, segundos))
