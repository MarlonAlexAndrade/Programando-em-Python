numero = int(input("Digite um numero par: "))
i = 0

if numero % 2 == 0 and numero > 0:
    while numero > i:   
        if numero % 2 == 0:
            print(f'O numero {numero} é par')
        
        numero -= 1           
else:
    print("Não é um numero par!")
    