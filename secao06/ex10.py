i = 0
x = 2
soma_pares = 0

while i < 50:   
    if x % 2 == 0:
        soma_pares += x
        i += 1       
    x += 1

print(f'A soma dos pares é de {soma_pares}')
