import random

lista = [0, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9, 10]
print(f'Lista gerada: {lista}')

duplicados = []
unicos = []

for i in lista:
    if i in unicos:
        duplicados.append(i)
    else:
        unicos.append(i)
            
print(f'Números únicos: {unicos}')
print(f'Números duplicados: {duplicados}')
