multiplo = False
numero = 2

while multiplo == False:
    if 11 %  numero == 0 or 13 % numero == 0 or 17 % numero == 0:
        print(numero)
        multiplo = True
    numero += 1
    