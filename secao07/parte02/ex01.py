matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

contador = 0
for lista in matriz:
    for valor in lista:
       if valor > 10:
           print(valor)
           contador += 1 

print(f'A quantidade de numeros acima de 10 é de: {contador}')
