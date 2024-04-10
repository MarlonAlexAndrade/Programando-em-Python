salario_carlos = 1200
salario_joao = 400
mes = 0

investimento_joao = salario_joao 
investimento_carlos = salario_carlos 

while investimento_joao < investimento_carlos:
    mes += 1

    investimento_joao *= 1.05
    investimento_carlos  *= 1.02 

    #Caso investimento for feito todo mes
    investimento_joao += 400
    investimento_carlos += 1200    

print(f'A quantidade e meses nescessarios para o investimento do joao passar o do carlos é de {mes} meses')