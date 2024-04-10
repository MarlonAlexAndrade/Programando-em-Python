numero = int(input("Digite um numero: "))

if numero < 2 : 
    print("Digite um numero maior que 1")
elif numero % 2 != 0: 
    print(f'O numero {numero} é primo!')
else:
    print(f'O numero não é primo!')
    