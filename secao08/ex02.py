def meses(mes):
    if mes == 1:
        return "Janeiro"
    elif mes == 2:
        return "Fevereiro"
    elif mes == 3:
        return "Março"
    elif mes == 4:
        return "Abril"
    elif mes == 5:
        return "Maio"
    elif mes == 6:
        return "Junho"
    elif mes == 7:
        return "Julho"
    elif mes == 8:
        return "Agosto"
    elif mes == 9:
        return "Setembro"
    elif mes == 10:
        return "Outubro"
    elif mes == 11:
        return "Novembro"
    elif mes == 12:
        return "Dezembro"
    else:
        return "Digite um numero valido"
    
def data_extenso(dia, mes, ano):
    return f'{dia} de {meses(mes)} de {ano}'


dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))

print({data_extenso(dia, mes, ano)})

