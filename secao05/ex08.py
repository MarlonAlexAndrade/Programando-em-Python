i = False

while i == False:
    nota01 = float(input("Digite a primeira nota: "))
    if nota01 >= 0 and nota01 <= 10: 
        i += 1

        nota02 = float(input("Digite a segunda nota: "))
        if nota02 >= 0 and nota02 <= 10:
            media = (nota01 + nota02) / 2
            print(f'A média é de {media}')
            i += 1
        else:
            print(f'O numero {nota02} é invalido!')
            i = True
    else:
        print(f'O numero {nota01} é invalido!')
        i = True
    
    
