i = 1
soma = 0
numero = 1000

for i in range(i, numero):
    if i % 3 == 0 and i % 5 == 0:
        soma += i
    
    i += 1

print(f'A soma dos divisores é de {soma}')