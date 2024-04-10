dia = int(input("Digite o numero de um dia da semana: "))

def switch(dia):
    if dia == 1:
        return "Domingo"
    elif dia == 2:
        return "Segunda-Feira"
    elif dia == 3:
        return "Terça-Feira"
    elif dia == 4:
        return "Quarta-Feira"
    elif dia == 5:
        return "Quinta-Feira"
    elif dia == 6:
        return "Sexta-Feira"
    elif dia == 7:
        return "Sabado"
    else:
        return "Digite um numero valido"
    
print(switch(dia))
