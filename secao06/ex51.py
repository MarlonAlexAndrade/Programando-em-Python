salario = 2000
porcentagem = 0.015

for i in range(1995, 2025):
    salario += salario * porcentagem
    porcentagem = porcentagem * 2


print(f'O salario dele será de {salario}')
