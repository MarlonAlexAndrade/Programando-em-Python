dia = int(input("Digite o mês em numero: "))

def switch(dia):
    if dia == 1:
        return "Janeiro"
    elif dia == 2:
        return "Fevereiro"
    elif dia == 3:
        return "Março"
    elif dia == 4:
        return "Abril"
    elif dia == 5:
        return "Maio"
    elif dia == 6:
        return "Junho"
    elif dia == 7:
        return "Julho"
    elif dia == 8:
        return "Agosto"
    elif dia == 9:
        return "Setembro"
    elif dia == 10:
        return "Outubro"
    elif dia == 11:
        return "Novembro"
    elif dia == 12:
        return "Dezembro"
    else:
        return "Digite um numero valido"
    
print(switch(dia))
