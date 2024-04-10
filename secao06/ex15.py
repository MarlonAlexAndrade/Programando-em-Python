numero = int(input("Digite um numero impar: "))
i = 0

if numero % 2 != 0 and numero > 0:
    while i < numero+1:   
        if i % 2 != 0:
            print(f'O numero {i} é impar')
        
        i += 1           
else:
    print("Não é um numero impar!")
    